DROP TABLE IF EXISTS startup;
-- DROP TABLE IF EXISTS investor;

CREATE TABLE startup (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    startup_name TEXT NOT NULL,
    web_address TEXT NOT NULL,
    pitch TEXT NOT NULL,
    stage TEXT NOT NULL,
    founding_date DATE NOT NULL,
    incorporated TEXT NOT NULL,
    county TEXT NOT NULL,
    user_title TEXT NOT NULL,
    user_role TEXT NOT NULL,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL,
    user_bio TEXT NOT NULL,
    phone_number TEXT NOT NULL,
    linkedin_address TEXT NOT NULL,
    elevator_pitch TEXT NOT NULL,
    reason_for_attendance TEXT NOT NULL,
);

-- CREATE TABLE investor (
--     id INTEGER PRIMARY KEY AUTOINCREMENT,
--     motivation TEXT NOT NULL,
--     first_name TEXT NOT NULL,
--     last_name TEXT NOT NULL,
--     email TEXT NOT NULL,
--     employment_status TEXT NOT NULL,
--     degree DATE NOT NULL,
--     organization TEXT NOT NULL,
--     organization_website TEXT NOT NULL,
--     user_bio TEXT NOT NULL,
--     reason_for_applying TEXT NOT NULL,
-- );

-- . venv/bin/activate