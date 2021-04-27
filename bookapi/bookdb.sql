--
-- PostgreSQL database dump
--

-- Dumped from database version 12.6 (Ubuntu 12.6-0ubuntu0.20.04.1)
-- Dumped by pg_dump version 12.6 (Ubuntu 12.6-0ubuntu0.20.04.1)

-- Started on 2021-04-27 18:40:48 GMT

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 225 (class 1259 OID 18205)
-- Name: api_inventory; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.api_inventory (
    id bigint NOT NULL,
    title character varying(200) NOT NULL,
    author character varying(200) NOT NULL,
    publisher character varying(200) NOT NULL,
    edition character varying(200) NOT NULL,
    category character varying(200) NOT NULL,
    covertype character varying(200) NOT NULL,
    created_date timestamp with time zone NOT NULL,
    added_by_id integer NOT NULL
);


ALTER TABLE public.api_inventory OWNER TO postgres;

--
-- TOC entry 224 (class 1259 OID 18203)
-- Name: api_inventory_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.api_inventory_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.api_inventory_id_seq OWNER TO postgres;

--
-- TOC entry 3122 (class 0 OID 0)
-- Dependencies: 224
-- Name: api_inventory_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.api_inventory_id_seq OWNED BY public.api_inventory.id;


--
-- TOC entry 2984 (class 2604 OID 18208)
-- Name: api_inventory id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_inventory ALTER COLUMN id SET DEFAULT nextval('public.api_inventory_id_seq'::regclass);


--
-- TOC entry 3116 (class 0 OID 18205)
-- Dependencies: 225
-- Data for Name: api_inventory; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.api_inventory (id, title, author, publisher, edition, category, covertype, created_date, added_by_id) FROM stdin;
1	Data Analyst	Jed	Ed	Vol 1	Article	Soft	2021-04-15 17:04:00+00	1
2	Highcharts Demo	Ed	Abi	Vol 2	Love	HArd	2021-04-14 19:59:00+00	2
3	Data Analyst	Ed	Abi	Vol 2	Love	Soft	2021-04-28 16:07:00+00	1
\.


--
-- TOC entry 3123 (class 0 OID 0)
-- Dependencies: 224
-- Name: api_inventory_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.api_inventory_id_seq', 3, true);


--
-- TOC entry 2987 (class 2606 OID 18213)
-- Name: api_inventory api_inventory_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_inventory
    ADD CONSTRAINT api_inventory_pkey PRIMARY KEY (id);


--
-- TOC entry 2985 (class 1259 OID 18219)
-- Name: api_inventory_added_by_id_9e541940; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX api_inventory_added_by_id_9e541940 ON public.api_inventory USING btree (added_by_id);


--
-- TOC entry 2988 (class 2606 OID 18214)
-- Name: api_inventory api_inventory_added_by_id_9e541940_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_inventory
    ADD CONSTRAINT api_inventory_added_by_id_9e541940_fk_auth_user_id FOREIGN KEY (added_by_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


-- Completed on 2021-04-27 18:40:48 GMT

--
-- PostgreSQL database dump complete
--

