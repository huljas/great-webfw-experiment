# Be sure to restart your server when you modify this file.

# Your secret key for verifying cookie session data integrity.
# If you change this key, all old sessions will become invalid!
# Make sure the secret is at least 30 characters and all random, 
# no regular words or you'll be exposed to dictionary attacks.
ActionController::Base.session = {
  :key         => '_rails-fibo_session',
  :secret      => '059cb3533704db9364d84aa64adeb6f1f585eaca5283873343159186dab5b1267e2e28401cc897a14c7ab9f1c2d712700e1b18a9c2882c16eb57f9c091ebdf10'
}

# Use the database for sessions instead of the cookie-based default,
# which shouldn't be used to store highly confidential information
# (create the session table with "rake db:sessions:create")
# ActionController::Base.session_store = :active_record_store
