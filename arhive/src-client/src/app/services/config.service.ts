import { Injectable } from '@angular/core';
import { Config, ConfigurationGoogleProvider, ConfigurationLocaleProvider, ConfigurationsProviders, PROVIDERS } from '../models/config';
import { HttpBackend, HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ConfigService {
  private appConfig: Config | undefined;
  private _providers: ConfigurationsProviders = {
    locale: undefined,
    google: undefined
  };

  private httpBackEnd: HttpClient;

  constructor(
    public handler: HttpBackend
  ) {
    this.httpBackEnd = new HttpClient(handler);
  }


  loadConfig(): Promise<Config> {
    console.log("Start load config")
    return new Promise((resolve, reject) => {
      this.httpBackEnd.get<Config>('assets/config.json')
        .toPromise()
        .then(
          async (config: Config | undefined) => {
            if (config) {
              this.appConfig = config;
              this.httpBackEnd.get<ConfigurationLocaleProvider>(config.providers.locale.configurationUrl).subscribe((data: ConfigurationLocaleProvider) => {
                this._providers.locale = data;
                resolve(this.appConfig as Config);
              });
            }
          },
          (err) => { 
            console.log('Failed to load config.json. ' + err);
            reject(err);
          }
        );
    })
  }

  get params(): Config {
    if (!this.appConfig) { throw Error('Trying to use config, but it was not yet loaded!') }
    return this.appConfig;
  }

  getProvideConfiguration(provider: PROVIDERS): null | ConfigurationLocaleProvider | ConfigurationGoogleProvider {
    if (provider in this._providers && this._providers[provider]) {
      return this._providers[provider];
    }
    return null
  }
}
