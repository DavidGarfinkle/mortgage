CREATE TABLE transactions (
	id PRIMARY SERIAL KEY,
	date DATE,
	amount MONEY,
	currency CHAR(3),
	merchant VARCHAR(80),
	subscription INTERVAL,
	reimbursement FOREIGN KEY REFERENCES cashflow.transactions,
	notes TEXT,
	tags TEXT[]
);
