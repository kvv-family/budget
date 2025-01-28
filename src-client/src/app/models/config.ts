
export type PROVIDERS = "locale" | "google";

export interface ConfigurationLocaleProvider {
    issuer: string;
    authorization_endpoint: string;
    token_endpoint: string;
    userinfo_endpoint: string;
    jwks_uri: string;
} 

export interface ConfigurationGoogleProvider {}

export interface ConfigurationsProviders {
    locale: ConfigurationLocaleProvider | undefined;
    google: ConfigurationGoogleProvider | undefined;
}

interface ProviderModel {
    configurationUrl: string;
    client_id: string;
    scope: string;
    redirect_url: string;
}

interface Providers {
    locale: ProviderModel;
}

export interface Config {
    providers: Providers
}