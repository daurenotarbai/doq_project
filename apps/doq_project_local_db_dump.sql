PGDMP     ,    #                z            doq_project_local_db    13.2    13.2 �    �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    943271    doq_project_local_db    DATABASE     q   CREATE DATABASE doq_project_local_db WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'Russian_Russia.1251';
 $   DROP DATABASE doq_project_local_db;
                postgres    false            �            1259    943303 
   auth_group    TABLE     f   CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(150) NOT NULL
);
    DROP TABLE public.auth_group;
       public         heap    postgres    false            �            1259    943301    auth_group_id_seq    SEQUENCE     �   CREATE SEQUENCE public.auth_group_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public.auth_group_id_seq;
       public          postgres    false    207            �           0    0    auth_group_id_seq    SEQUENCE OWNED BY     G   ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;
          public          postgres    false    206            �            1259    943313    auth_group_permissions    TABLE     �   CREATE TABLE public.auth_group_permissions (
    id bigint NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);
 *   DROP TABLE public.auth_group_permissions;
       public         heap    postgres    false            �            1259    943311    auth_group_permissions_id_seq    SEQUENCE     �   CREATE SEQUENCE public.auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 4   DROP SEQUENCE public.auth_group_permissions_id_seq;
       public          postgres    false    209            �           0    0    auth_group_permissions_id_seq    SEQUENCE OWNED BY     _   ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;
          public          postgres    false    208            �            1259    943295    auth_permission    TABLE     �   CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);
 #   DROP TABLE public.auth_permission;
       public         heap    postgres    false            �            1259    943293    auth_permission_id_seq    SEQUENCE     �   CREATE SEQUENCE public.auth_permission_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 -   DROP SEQUENCE public.auth_permission_id_seq;
       public          postgres    false    205            �           0    0    auth_permission_id_seq    SEQUENCE OWNED BY     Q   ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;
          public          postgres    false    204            �            1259    943321 	   auth_user    TABLE     �  CREATE TABLE public.auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(150) NOT NULL,
    last_name character varying(150) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);
    DROP TABLE public.auth_user;
       public         heap    postgres    false            �            1259    943331    auth_user_groups    TABLE     ~   CREATE TABLE public.auth_user_groups (
    id bigint NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);
 $   DROP TABLE public.auth_user_groups;
       public         heap    postgres    false            �            1259    943329    auth_user_groups_id_seq    SEQUENCE     �   CREATE SEQUENCE public.auth_user_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 .   DROP SEQUENCE public.auth_user_groups_id_seq;
       public          postgres    false    213            �           0    0    auth_user_groups_id_seq    SEQUENCE OWNED BY     S   ALTER SEQUENCE public.auth_user_groups_id_seq OWNED BY public.auth_user_groups.id;
          public          postgres    false    212            �            1259    943319    auth_user_id_seq    SEQUENCE     �   CREATE SEQUENCE public.auth_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.auth_user_id_seq;
       public          postgres    false    211            �           0    0    auth_user_id_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE public.auth_user_id_seq OWNED BY public.auth_user.id;
          public          postgres    false    210            �            1259    943339    auth_user_user_permissions    TABLE     �   CREATE TABLE public.auth_user_user_permissions (
    id bigint NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);
 .   DROP TABLE public.auth_user_user_permissions;
       public         heap    postgres    false            �            1259    943337 !   auth_user_user_permissions_id_seq    SEQUENCE     �   CREATE SEQUENCE public.auth_user_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 8   DROP SEQUENCE public.auth_user_user_permissions_id_seq;
       public          postgres    false    215            �           0    0 !   auth_user_user_permissions_id_seq    SEQUENCE OWNED BY     g   ALTER SEQUENCE public.auth_user_user_permissions_id_seq OWNED BY public.auth_user_user_permissions.id;
          public          postgres    false    214            �            1259    943471    clinics_address    TABLE     �   CREATE TABLE public.clinics_address (
    id bigint NOT NULL,
    city character varying(255),
    address character varying(255),
    clinic_id bigint NOT NULL
);
 #   DROP TABLE public.clinics_address;
       public         heap    postgres    false            �            1259    943469    clinics_address_id_seq    SEQUENCE        CREATE SEQUENCE public.clinics_address_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 -   DROP SEQUENCE public.clinics_address_id_seq;
       public          postgres    false    227            �           0    0    clinics_address_id_seq    SEQUENCE OWNED BY     Q   ALTER SEQUENCE public.clinics_address_id_seq OWNED BY public.clinics_address.id;
          public          postgres    false    226            �            1259    943614    clinics_appointmentdoctortime    TABLE     |   CREATE TABLE public.clinics_appointmentdoctortime (
    id bigint NOT NULL,
    date date NOT NULL,
    doctor_id bigint
);
 1   DROP TABLE public.clinics_appointmentdoctortime;
       public         heap    postgres    false            �            1259    943612 $   clinics_appointmentdoctortime_id_seq    SEQUENCE     �   CREATE SEQUENCE public.clinics_appointmentdoctortime_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 ;   DROP SEQUENCE public.clinics_appointmentdoctortime_id_seq;
       public          postgres    false    240            �           0    0 $   clinics_appointmentdoctortime_id_seq    SEQUENCE OWNED BY     m   ALTER SEQUENCE public.clinics_appointmentdoctortime_id_seq OWNED BY public.clinics_appointmentdoctortime.id;
          public          postgres    false    239            �            1259    943622 #   clinics_appointmentdoctortime_times    TABLE     �   CREATE TABLE public.clinics_appointmentdoctortime_times (
    id bigint NOT NULL,
    appointmentdoctortime_id bigint NOT NULL,
    appointmenttime_id bigint NOT NULL
);
 7   DROP TABLE public.clinics_appointmentdoctortime_times;
       public         heap    postgres    false            �            1259    943620 *   clinics_appointmentdoctortime_times_id_seq    SEQUENCE     �   CREATE SEQUENCE public.clinics_appointmentdoctortime_times_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 A   DROP SEQUENCE public.clinics_appointmentdoctortime_times_id_seq;
       public          postgres    false    242            �           0    0 *   clinics_appointmentdoctortime_times_id_seq    SEQUENCE OWNED BY     y   ALTER SEQUENCE public.clinics_appointmentdoctortime_times_id_seq OWNED BY public.clinics_appointmentdoctortime_times.id;
          public          postgres    false    241            �            1259    943432    clinics_appointmenttime    TABLE     x   CREATE TABLE public.clinics_appointmenttime (
    id bigint NOT NULL,
    start_time time without time zone NOT NULL
);
 +   DROP TABLE public.clinics_appointmenttime;
       public         heap    postgres    false            �            1259    943430    clinics_appointmenttime_id_seq    SEQUENCE     �   CREATE SEQUENCE public.clinics_appointmenttime_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 5   DROP SEQUENCE public.clinics_appointmenttime_id_seq;
       public          postgres    false    219            �           0    0    clinics_appointmenttime_id_seq    SEQUENCE OWNED BY     a   ALTER SEQUENCE public.clinics_appointmenttime_id_seq OWNED BY public.clinics_appointmenttime.id;
          public          postgres    false    218            �            1259    943440    clinics_clinic    TABLE     �  CREATE TABLE public.clinics_clinic (
    id bigint NOT NULL,
    created_at timestamp with time zone NOT NULL,
    changed_at timestamp with time zone NOT NULL,
    phone character varying(20) NOT NULL,
    work_phone character varying(20) NOT NULL,
    name character varying(50) NOT NULL,
    description text NOT NULL,
    logo character varying(100) NOT NULL,
    user_id integer,
    is_active boolean NOT NULL
);
 "   DROP TABLE public.clinics_clinic;
       public         heap    postgres    false            �            1259    943438    clinics_clinic_id_seq    SEQUENCE     ~   CREATE SEQUENCE public.clinics_clinic_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 ,   DROP SEQUENCE public.clinics_clinic_id_seq;
       public          postgres    false    221            �           0    0    clinics_clinic_id_seq    SEQUENCE OWNED BY     O   ALTER SEQUENCE public.clinics_clinic_id_seq OWNED BY public.clinics_clinic.id;
          public          postgres    false    220            �            1259    943463    clinics_clinicphoto    TABLE     �   CREATE TABLE public.clinics_clinicphoto (
    id bigint NOT NULL,
    image character varying(100) NOT NULL,
    clinic_id bigint NOT NULL
);
 '   DROP TABLE public.clinics_clinicphoto;
       public         heap    postgres    false            �            1259    943461    clinics_clinicphoto_id_seq    SEQUENCE     �   CREATE SEQUENCE public.clinics_clinicphoto_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 1   DROP SEQUENCE public.clinics_clinicphoto_id_seq;
       public          postgres    false    225            �           0    0    clinics_clinicphoto_id_seq    SEQUENCE OWNED BY     Y   ALTER SEQUENCE public.clinics_clinicphoto_id_seq OWNED BY public.clinics_clinicphoto.id;
          public          postgres    false    224            �            1259    943451    clinics_doctor    TABLE     �  CREATE TABLE public.clinics_doctor (
    id bigint NOT NULL,
    first_name character varying(255) NOT NULL,
    last_name character varying(255) NOT NULL,
    middle_name character varying(255) NOT NULL,
    gender character varying(10),
    experience_years smallint,
    consultation_fee numeric(10,2) NOT NULL,
    clinic_id bigint NOT NULL,
    photo character varying(100),
    CONSTRAINT clinics_doctor_experience_years_check CHECK ((experience_years >= 0))
);
 "   DROP TABLE public.clinics_doctor;
       public         heap    postgres    false            �            1259    943449    clinics_doctor_id_seq    SEQUENCE     ~   CREATE SEQUENCE public.clinics_doctor_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 ,   DROP SEQUENCE public.clinics_doctor_id_seq;
       public          postgres    false    223            �           0    0    clinics_doctor_id_seq    SEQUENCE OWNED BY     O   ALTER SEQUENCE public.clinics_doctor_id_seq OWNED BY public.clinics_doctor.id;
          public          postgres    false    222            �            1259    943579    clinics_doctor_procedures    TABLE     �   CREATE TABLE public.clinics_doctor_procedures (
    id bigint NOT NULL,
    doctor_id bigint NOT NULL,
    procedure_id bigint NOT NULL
);
 -   DROP TABLE public.clinics_doctor_procedures;
       public         heap    postgres    false            �            1259    943577     clinics_doctor_procedures_id_seq    SEQUENCE     �   CREATE SEQUENCE public.clinics_doctor_procedures_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 7   DROP SEQUENCE public.clinics_doctor_procedures_id_seq;
       public          postgres    false    238            �           0    0     clinics_doctor_procedures_id_seq    SEQUENCE OWNED BY     e   ALTER SEQUENCE public.clinics_doctor_procedures_id_seq OWNED BY public.clinics_doctor_procedures.id;
          public          postgres    false    237            �            1259    943557    clinics_doctor_specialities    TABLE     �   CREATE TABLE public.clinics_doctor_specialities (
    id bigint NOT NULL,
    doctor_id bigint NOT NULL,
    speciality_id bigint NOT NULL
);
 /   DROP TABLE public.clinics_doctor_specialities;
       public         heap    postgres    false            �            1259    943555 "   clinics_doctor_specialities_id_seq    SEQUENCE     �   CREATE SEQUENCE public.clinics_doctor_specialities_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 9   DROP SEQUENCE public.clinics_doctor_specialities_id_seq;
       public          postgres    false    236            �           0    0 "   clinics_doctor_specialities_id_seq    SEQUENCE OWNED BY     i   ALTER SEQUENCE public.clinics_doctor_specialities_id_seq OWNED BY public.clinics_doctor_specialities.id;
          public          postgres    false    235            �            1259    943543    clinics_procedure    TABLE     �   CREATE TABLE public.clinics_procedure (
    id bigint NOT NULL,
    name character varying(255) NOT NULL,
    parent_id bigint,
    is_specialty boolean NOT NULL
);
 %   DROP TABLE public.clinics_procedure;
       public         heap    postgres    false            �            1259    943541    clinics_procedure_id_seq    SEQUENCE     �   CREATE SEQUENCE public.clinics_procedure_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 /   DROP SEQUENCE public.clinics_procedure_id_seq;
       public          postgres    false    234            �           0    0    clinics_procedure_id_seq    SEQUENCE OWNED BY     U   ALTER SEQUENCE public.clinics_procedure_id_seq OWNED BY public.clinics_procedure.id;
          public          postgres    false    233            �            1259    943535    clinics_speciality    TABLE     m   CREATE TABLE public.clinics_speciality (
    id bigint NOT NULL,
    name character varying(255) NOT NULL
);
 &   DROP TABLE public.clinics_speciality;
       public         heap    postgres    false            �            1259    943533    clinics_speciality_id_seq    SEQUENCE     �   CREATE SEQUENCE public.clinics_speciality_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 0   DROP SEQUENCE public.clinics_speciality_id_seq;
       public          postgres    false    232            �           0    0    clinics_speciality_id_seq    SEQUENCE OWNED BY     W   ALTER SEQUENCE public.clinics_speciality_id_seq OWNED BY public.clinics_speciality.id;
          public          postgres    false    231            �            1259    943399    django_admin_log    TABLE     �  CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);
 $   DROP TABLE public.django_admin_log;
       public         heap    postgres    false            �            1259    943397    django_admin_log_id_seq    SEQUENCE     �   CREATE SEQUENCE public.django_admin_log_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 .   DROP SEQUENCE public.django_admin_log_id_seq;
       public          postgres    false    217            �           0    0    django_admin_log_id_seq    SEQUENCE OWNED BY     S   ALTER SEQUENCE public.django_admin_log_id_seq OWNED BY public.django_admin_log.id;
          public          postgres    false    216            �            1259    943285    django_content_type    TABLE     �   CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);
 '   DROP TABLE public.django_content_type;
       public         heap    postgres    false            �            1259    943283    django_content_type_id_seq    SEQUENCE     �   CREATE SEQUENCE public.django_content_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 1   DROP SEQUENCE public.django_content_type_id_seq;
       public          postgres    false    203            �           0    0    django_content_type_id_seq    SEQUENCE OWNED BY     Y   ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;
          public          postgres    false    202            �            1259    943274    django_migrations    TABLE     �   CREATE TABLE public.django_migrations (
    id bigint NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);
 %   DROP TABLE public.django_migrations;
       public         heap    postgres    false            �            1259    943272    django_migrations_id_seq    SEQUENCE     �   CREATE SEQUENCE public.django_migrations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 /   DROP SEQUENCE public.django_migrations_id_seq;
       public          postgres    false    201            �           0    0    django_migrations_id_seq    SEQUENCE OWNED BY     U   ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;
          public          postgres    false    200            �            1259    943522    django_session    TABLE     �   CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);
 "   DROP TABLE public.django_session;
       public         heap    postgres    false            �            1259    943502    patients_appointment    TABLE     I  CREATE TABLE public.patients_appointment (
    id bigint NOT NULL,
    created_at timestamp with time zone NOT NULL,
    changed_at timestamp with time zone NOT NULL,
    first_name character varying(255) NOT NULL,
    iin character varying(12) NOT NULL,
    appointment_time_id bigint NOT NULL,
    doctor_id bigint NOT NULL
);
 (   DROP TABLE public.patients_appointment;
       public         heap    postgres    false            �            1259    943500    patients_appointment_id_seq    SEQUENCE     �   CREATE SEQUENCE public.patients_appointment_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 2   DROP SEQUENCE public.patients_appointment_id_seq;
       public          postgres    false    229            �           0    0    patients_appointment_id_seq    SEQUENCE OWNED BY     [   ALTER SEQUENCE public.patients_appointment_id_seq OWNED BY public.patients_appointment.id;
          public          postgres    false    228            �           2604    943306    auth_group id    DEFAULT     n   ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);
 <   ALTER TABLE public.auth_group ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    207    206    207            �           2604    943316    auth_group_permissions id    DEFAULT     �   ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);
 H   ALTER TABLE public.auth_group_permissions ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    209    208    209            �           2604    943298    auth_permission id    DEFAULT     x   ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);
 A   ALTER TABLE public.auth_permission ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    204    205    205            �           2604    943324    auth_user id    DEFAULT     l   ALTER TABLE ONLY public.auth_user ALTER COLUMN id SET DEFAULT nextval('public.auth_user_id_seq'::regclass);
 ;   ALTER TABLE public.auth_user ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    210    211    211            �           2604    943334    auth_user_groups id    DEFAULT     z   ALTER TABLE ONLY public.auth_user_groups ALTER COLUMN id SET DEFAULT nextval('public.auth_user_groups_id_seq'::regclass);
 B   ALTER TABLE public.auth_user_groups ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    213    212    213            �           2604    943342    auth_user_user_permissions id    DEFAULT     �   ALTER TABLE ONLY public.auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_user_user_permissions_id_seq'::regclass);
 L   ALTER TABLE public.auth_user_user_permissions ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    214    215    215            �           2604    943474    clinics_address id    DEFAULT     x   ALTER TABLE ONLY public.clinics_address ALTER COLUMN id SET DEFAULT nextval('public.clinics_address_id_seq'::regclass);
 A   ALTER TABLE public.clinics_address ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    226    227    227            �           2604    943617     clinics_appointmentdoctortime id    DEFAULT     �   ALTER TABLE ONLY public.clinics_appointmentdoctortime ALTER COLUMN id SET DEFAULT nextval('public.clinics_appointmentdoctortime_id_seq'::regclass);
 O   ALTER TABLE public.clinics_appointmentdoctortime ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    239    240    240            �           2604    943625 &   clinics_appointmentdoctortime_times id    DEFAULT     �   ALTER TABLE ONLY public.clinics_appointmentdoctortime_times ALTER COLUMN id SET DEFAULT nextval('public.clinics_appointmentdoctortime_times_id_seq'::regclass);
 U   ALTER TABLE public.clinics_appointmentdoctortime_times ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    241    242    242            �           2604    943435    clinics_appointmenttime id    DEFAULT     �   ALTER TABLE ONLY public.clinics_appointmenttime ALTER COLUMN id SET DEFAULT nextval('public.clinics_appointmenttime_id_seq'::regclass);
 I   ALTER TABLE public.clinics_appointmenttime ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    218    219    219            �           2604    943443    clinics_clinic id    DEFAULT     v   ALTER TABLE ONLY public.clinics_clinic ALTER COLUMN id SET DEFAULT nextval('public.clinics_clinic_id_seq'::regclass);
 @   ALTER TABLE public.clinics_clinic ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    221    220    221            �           2604    943466    clinics_clinicphoto id    DEFAULT     �   ALTER TABLE ONLY public.clinics_clinicphoto ALTER COLUMN id SET DEFAULT nextval('public.clinics_clinicphoto_id_seq'::regclass);
 E   ALTER TABLE public.clinics_clinicphoto ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    225    224    225            �           2604    943454    clinics_doctor id    DEFAULT     v   ALTER TABLE ONLY public.clinics_doctor ALTER COLUMN id SET DEFAULT nextval('public.clinics_doctor_id_seq'::regclass);
 @   ALTER TABLE public.clinics_doctor ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    223    222    223            �           2604    943582    clinics_doctor_procedures id    DEFAULT     �   ALTER TABLE ONLY public.clinics_doctor_procedures ALTER COLUMN id SET DEFAULT nextval('public.clinics_doctor_procedures_id_seq'::regclass);
 K   ALTER TABLE public.clinics_doctor_procedures ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    237    238    238            �           2604    943560    clinics_doctor_specialities id    DEFAULT     �   ALTER TABLE ONLY public.clinics_doctor_specialities ALTER COLUMN id SET DEFAULT nextval('public.clinics_doctor_specialities_id_seq'::regclass);
 M   ALTER TABLE public.clinics_doctor_specialities ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    236    235    236            �           2604    943546    clinics_procedure id    DEFAULT     |   ALTER TABLE ONLY public.clinics_procedure ALTER COLUMN id SET DEFAULT nextval('public.clinics_procedure_id_seq'::regclass);
 C   ALTER TABLE public.clinics_procedure ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    233    234    234            �           2604    943538    clinics_speciality id    DEFAULT     ~   ALTER TABLE ONLY public.clinics_speciality ALTER COLUMN id SET DEFAULT nextval('public.clinics_speciality_id_seq'::regclass);
 D   ALTER TABLE public.clinics_speciality ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    231    232    232            �           2604    943402    django_admin_log id    DEFAULT     z   ALTER TABLE ONLY public.django_admin_log ALTER COLUMN id SET DEFAULT nextval('public.django_admin_log_id_seq'::regclass);
 B   ALTER TABLE public.django_admin_log ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    217    216    217            �           2604    943288    django_content_type id    DEFAULT     �   ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);
 E   ALTER TABLE public.django_content_type ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    203    202    203            �           2604    943277    django_migrations id    DEFAULT     |   ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);
 C   ALTER TABLE public.django_migrations ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    200    201    201            �           2604    943505    patients_appointment id    DEFAULT     �   ALTER TABLE ONLY public.patients_appointment ALTER COLUMN id SET DEFAULT nextval('public.patients_appointment_id_seq'::regclass);
 F   ALTER TABLE public.patients_appointment ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    228    229    229            �          0    943303 
   auth_group 
   TABLE DATA           .   COPY public.auth_group (id, name) FROM stdin;
    public          postgres    false    207   �-      �          0    943313    auth_group_permissions 
   TABLE DATA           M   COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
    public          postgres    false    209   �-      �          0    943295    auth_permission 
   TABLE DATA           N   COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
    public          postgres    false    205   .      �          0    943321 	   auth_user 
   TABLE DATA           �   COPY public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
    public          postgres    false    211   1      �          0    943331    auth_user_groups 
   TABLE DATA           A   COPY public.auth_user_groups (id, user_id, group_id) FROM stdin;
    public          postgres    false    213   2      �          0    943339    auth_user_user_permissions 
   TABLE DATA           P   COPY public.auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
    public          postgres    false    215   +2      �          0    943471    clinics_address 
   TABLE DATA           G   COPY public.clinics_address (id, city, address, clinic_id) FROM stdin;
    public          postgres    false    227   H2      �          0    943614    clinics_appointmentdoctortime 
   TABLE DATA           L   COPY public.clinics_appointmentdoctortime (id, date, doctor_id) FROM stdin;
    public          postgres    false    240   �2      �          0    943622 #   clinics_appointmentdoctortime_times 
   TABLE DATA           o   COPY public.clinics_appointmentdoctortime_times (id, appointmentdoctortime_id, appointmenttime_id) FROM stdin;
    public          postgres    false    242   E3      �          0    943432    clinics_appointmenttime 
   TABLE DATA           A   COPY public.clinics_appointmenttime (id, start_time) FROM stdin;
    public          postgres    false    219   �3      �          0    943440    clinics_clinic 
   TABLE DATA           �   COPY public.clinics_clinic (id, created_at, changed_at, phone, work_phone, name, description, logo, user_id, is_active) FROM stdin;
    public          postgres    false    221   �4      �          0    943463    clinics_clinicphoto 
   TABLE DATA           C   COPY public.clinics_clinicphoto (id, image, clinic_id) FROM stdin;
    public          postgres    false    225   �9      �          0    943451    clinics_doctor 
   TABLE DATA           �   COPY public.clinics_doctor (id, first_name, last_name, middle_name, gender, experience_years, consultation_fee, clinic_id, photo) FROM stdin;
    public          postgres    false    223   �9      �          0    943579    clinics_doctor_procedures 
   TABLE DATA           P   COPY public.clinics_doctor_procedures (id, doctor_id, procedure_id) FROM stdin;
    public          postgres    false    238   �:      �          0    943557    clinics_doctor_specialities 
   TABLE DATA           S   COPY public.clinics_doctor_specialities (id, doctor_id, speciality_id) FROM stdin;
    public          postgres    false    236   ;      �          0    943543    clinics_procedure 
   TABLE DATA           N   COPY public.clinics_procedure (id, name, parent_id, is_specialty) FROM stdin;
    public          postgres    false    234   K;      �          0    943535    clinics_speciality 
   TABLE DATA           6   COPY public.clinics_speciality (id, name) FROM stdin;
    public          postgres    false    232   �;      �          0    943399    django_admin_log 
   TABLE DATA           �   COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
    public          postgres    false    217   �<      �          0    943285    django_content_type 
   TABLE DATA           C   COPY public.django_content_type (id, app_label, model) FROM stdin;
    public          postgres    false    203   �I      �          0    943274    django_migrations 
   TABLE DATA           C   COPY public.django_migrations (id, app, name, applied) FROM stdin;
    public          postgres    false    201   =J      �          0    943522    django_session 
   TABLE DATA           P   COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
    public          postgres    false    230   �M      �          0    943502    patients_appointment 
   TABLE DATA           {   COPY public.patients_appointment (id, created_at, changed_at, first_name, iin, appointment_time_id, doctor_id) FROM stdin;
    public          postgres    false    229   
Q      �           0    0    auth_group_id_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public.auth_group_id_seq', 1, true);
          public          postgres    false    206            �           0    0    auth_group_permissions_id_seq    SEQUENCE SET     L   SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 13, true);
          public          postgres    false    208            �           0    0    auth_permission_id_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('public.auth_permission_id_seq', 60, true);
          public          postgres    false    204            �           0    0    auth_user_groups_id_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('public.auth_user_groups_id_seq', 2, true);
          public          postgres    false    212                        0    0    auth_user_id_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('public.auth_user_id_seq', 3, true);
          public          postgres    false    210                       0    0 !   auth_user_user_permissions_id_seq    SEQUENCE SET     P   SELECT pg_catalog.setval('public.auth_user_user_permissions_id_seq', 1, false);
          public          postgres    false    214                       0    0    clinics_address_id_seq    SEQUENCE SET     D   SELECT pg_catalog.setval('public.clinics_address_id_seq', 3, true);
          public          postgres    false    226                       0    0 $   clinics_appointmentdoctortime_id_seq    SEQUENCE SET     U   SELECT pg_catalog.setval('public.clinics_appointmentdoctortime_id_seq', 2020, true);
          public          postgres    false    239                       0    0 *   clinics_appointmentdoctortime_times_id_seq    SEQUENCE SET     Z   SELECT pg_catalog.setval('public.clinics_appointmentdoctortime_times_id_seq', 107, true);
          public          postgres    false    241                       0    0    clinics_appointmenttime_id_seq    SEQUENCE SET     M   SELECT pg_catalog.setval('public.clinics_appointmenttime_id_seq', 48, true);
          public          postgres    false    218                       0    0    clinics_clinic_id_seq    SEQUENCE SET     C   SELECT pg_catalog.setval('public.clinics_clinic_id_seq', 2, true);
          public          postgres    false    220                       0    0    clinics_clinicphoto_id_seq    SEQUENCE SET     I   SELECT pg_catalog.setval('public.clinics_clinicphoto_id_seq', 1, false);
          public          postgres    false    224                       0    0    clinics_doctor_id_seq    SEQUENCE SET     C   SELECT pg_catalog.setval('public.clinics_doctor_id_seq', 3, true);
          public          postgres    false    222            	           0    0     clinics_doctor_procedures_id_seq    SEQUENCE SET     N   SELECT pg_catalog.setval('public.clinics_doctor_procedures_id_seq', 6, true);
          public          postgres    false    237            
           0    0 "   clinics_doctor_specialities_id_seq    SEQUENCE SET     P   SELECT pg_catalog.setval('public.clinics_doctor_specialities_id_seq', 7, true);
          public          postgres    false    235                       0    0    clinics_procedure_id_seq    SEQUENCE SET     F   SELECT pg_catalog.setval('public.clinics_procedure_id_seq', 5, true);
          public          postgres    false    233                       0    0    clinics_speciality_id_seq    SEQUENCE SET     H   SELECT pg_catalog.setval('public.clinics_speciality_id_seq', 11, true);
          public          postgres    false    231                       0    0    django_admin_log_id_seq    SEQUENCE SET     G   SELECT pg_catalog.setval('public.django_admin_log_id_seq', 151, true);
          public          postgres    false    216                       0    0    django_content_type_id_seq    SEQUENCE SET     I   SELECT pg_catalog.setval('public.django_content_type_id_seq', 15, true);
          public          postgres    false    202                       0    0    django_migrations_id_seq    SEQUENCE SET     G   SELECT pg_catalog.setval('public.django_migrations_id_seq', 36, true);
          public          postgres    false    200                       0    0    patients_appointment_id_seq    SEQUENCE SET     I   SELECT pg_catalog.setval('public.patients_appointment_id_seq', 1, true);
          public          postgres    false    228            �           2606    943428    auth_group auth_group_name_key 
   CONSTRAINT     Y   ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);
 H   ALTER TABLE ONLY public.auth_group DROP CONSTRAINT auth_group_name_key;
       public            postgres    false    207            �           2606    943355 R   auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);
 |   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq;
       public            postgres    false    209    209            �           2606    943318 2   auth_group_permissions auth_group_permissions_pkey 
   CONSTRAINT     p   ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);
 \   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissions_pkey;
       public            postgres    false    209            �           2606    943308    auth_group auth_group_pkey 
   CONSTRAINT     X   ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);
 D   ALTER TABLE ONLY public.auth_group DROP CONSTRAINT auth_group_pkey;
       public            postgres    false    207            �           2606    943346 F   auth_permission auth_permission_content_type_id_codename_01ab375a_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);
 p   ALTER TABLE ONLY public.auth_permission DROP CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq;
       public            postgres    false    205    205            �           2606    943300 $   auth_permission auth_permission_pkey 
   CONSTRAINT     b   ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);
 N   ALTER TABLE ONLY public.auth_permission DROP CONSTRAINT auth_permission_pkey;
       public            postgres    false    205            �           2606    943336 &   auth_user_groups auth_user_groups_pkey 
   CONSTRAINT     d   ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);
 P   ALTER TABLE ONLY public.auth_user_groups DROP CONSTRAINT auth_user_groups_pkey;
       public            postgres    false    213            �           2606    943370 @   auth_user_groups auth_user_groups_user_id_group_id_94350c0c_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq UNIQUE (user_id, group_id);
 j   ALTER TABLE ONLY public.auth_user_groups DROP CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq;
       public            postgres    false    213    213            �           2606    943326    auth_user auth_user_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);
 B   ALTER TABLE ONLY public.auth_user DROP CONSTRAINT auth_user_pkey;
       public            postgres    false    211            �           2606    943344 :   auth_user_user_permissions auth_user_user_permissions_pkey 
   CONSTRAINT     x   ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);
 d   ALTER TABLE ONLY public.auth_user_user_permissions DROP CONSTRAINT auth_user_user_permissions_pkey;
       public            postgres    false    215            �           2606    943384 Y   auth_user_user_permissions auth_user_user_permissions_user_id_permission_id_14a6b632_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq UNIQUE (user_id, permission_id);
 �   ALTER TABLE ONLY public.auth_user_user_permissions DROP CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq;
       public            postgres    false    215    215            �           2606    943422     auth_user auth_user_username_key 
   CONSTRAINT     _   ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);
 J   ALTER TABLE ONLY public.auth_user DROP CONSTRAINT auth_user_username_key;
       public            postgres    false    211            �           2606    943479 $   clinics_address clinics_address_pkey 
   CONSTRAINT     b   ALTER TABLE ONLY public.clinics_address
    ADD CONSTRAINT clinics_address_pkey PRIMARY KEY (id);
 N   ALTER TABLE ONLY public.clinics_address DROP CONSTRAINT clinics_address_pkey;
       public            postgres    false    227                       2606    943635 c   clinics_appointmentdoctortime_times clinics_appointmentdocto_appointmentdoctortime_id_13bfe18c_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.clinics_appointmentdoctortime_times
    ADD CONSTRAINT clinics_appointmentdocto_appointmentdoctortime_id_13bfe18c_uniq UNIQUE (appointmentdoctortime_id, appointmenttime_id);
 �   ALTER TABLE ONLY public.clinics_appointmentdoctortime_times DROP CONSTRAINT clinics_appointmentdocto_appointmentdoctortime_id_13bfe18c_uniq;
       public            postgres    false    242    242                       2606    943652 X   clinics_appointmentdoctortime clinics_appointmentdoctortime_doctor_id_date_e21c7887_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.clinics_appointmentdoctortime
    ADD CONSTRAINT clinics_appointmentdoctortime_doctor_id_date_e21c7887_uniq UNIQUE (doctor_id, date);
 �   ALTER TABLE ONLY public.clinics_appointmentdoctortime DROP CONSTRAINT clinics_appointmentdoctortime_doctor_id_date_e21c7887_uniq;
       public            postgres    false    240    240                       2606    943619 @   clinics_appointmentdoctortime clinics_appointmentdoctortime_pkey 
   CONSTRAINT     ~   ALTER TABLE ONLY public.clinics_appointmentdoctortime
    ADD CONSTRAINT clinics_appointmentdoctortime_pkey PRIMARY KEY (id);
 j   ALTER TABLE ONLY public.clinics_appointmentdoctortime DROP CONSTRAINT clinics_appointmentdoctortime_pkey;
       public            postgres    false    240                       2606    943627 L   clinics_appointmentdoctortime_times clinics_appointmentdoctortime_times_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public.clinics_appointmentdoctortime_times
    ADD CONSTRAINT clinics_appointmentdoctortime_times_pkey PRIMARY KEY (id);
 v   ALTER TABLE ONLY public.clinics_appointmentdoctortime_times DROP CONSTRAINT clinics_appointmentdoctortime_times_pkey;
       public            postgres    false    242            �           2606    943437 4   clinics_appointmenttime clinics_appointmenttime_pkey 
   CONSTRAINT     r   ALTER TABLE ONLY public.clinics_appointmenttime
    ADD CONSTRAINT clinics_appointmenttime_pkey PRIMARY KEY (id);
 ^   ALTER TABLE ONLY public.clinics_appointmenttime DROP CONSTRAINT clinics_appointmenttime_pkey;
       public            postgres    false    219            �           2606    943448 "   clinics_clinic clinics_clinic_pkey 
   CONSTRAINT     `   ALTER TABLE ONLY public.clinics_clinic
    ADD CONSTRAINT clinics_clinic_pkey PRIMARY KEY (id);
 L   ALTER TABLE ONLY public.clinics_clinic DROP CONSTRAINT clinics_clinic_pkey;
       public            postgres    false    221            �           2606    943468 ,   clinics_clinicphoto clinics_clinicphoto_pkey 
   CONSTRAINT     j   ALTER TABLE ONLY public.clinics_clinicphoto
    ADD CONSTRAINT clinics_clinicphoto_pkey PRIMARY KEY (id);
 V   ALTER TABLE ONLY public.clinics_clinicphoto DROP CONSTRAINT clinics_clinicphoto_pkey;
       public            postgres    false    225            �           2606    943460 "   clinics_doctor clinics_doctor_pkey 
   CONSTRAINT     `   ALTER TABLE ONLY public.clinics_doctor
    ADD CONSTRAINT clinics_doctor_pkey PRIMARY KEY (id);
 L   ALTER TABLE ONLY public.clinics_doctor DROP CONSTRAINT clinics_doctor_pkey;
       public            postgres    false    223                       2606    943586 X   clinics_doctor_procedures clinics_doctor_procedures_doctor_id_procedure_id_a5ed548c_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.clinics_doctor_procedures
    ADD CONSTRAINT clinics_doctor_procedures_doctor_id_procedure_id_a5ed548c_uniq UNIQUE (doctor_id, procedure_id);
 �   ALTER TABLE ONLY public.clinics_doctor_procedures DROP CONSTRAINT clinics_doctor_procedures_doctor_id_procedure_id_a5ed548c_uniq;
       public            postgres    false    238    238                       2606    943584 8   clinics_doctor_procedures clinics_doctor_procedures_pkey 
   CONSTRAINT     v   ALTER TABLE ONLY public.clinics_doctor_procedures
    ADD CONSTRAINT clinics_doctor_procedures_pkey PRIMARY KEY (id);
 b   ALTER TABLE ONLY public.clinics_doctor_procedures DROP CONSTRAINT clinics_doctor_procedures_pkey;
       public            postgres    false    238                       2606    943564 Z   clinics_doctor_specialities clinics_doctor_specialit_doctor_id_speciality_id_3b1d15f0_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.clinics_doctor_specialities
    ADD CONSTRAINT clinics_doctor_specialit_doctor_id_speciality_id_3b1d15f0_uniq UNIQUE (doctor_id, speciality_id);
 �   ALTER TABLE ONLY public.clinics_doctor_specialities DROP CONSTRAINT clinics_doctor_specialit_doctor_id_speciality_id_3b1d15f0_uniq;
       public            postgres    false    236    236            
           2606    943562 <   clinics_doctor_specialities clinics_doctor_specialities_pkey 
   CONSTRAINT     z   ALTER TABLE ONLY public.clinics_doctor_specialities
    ADD CONSTRAINT clinics_doctor_specialities_pkey PRIMARY KEY (id);
 f   ALTER TABLE ONLY public.clinics_doctor_specialities DROP CONSTRAINT clinics_doctor_specialities_pkey;
       public            postgres    false    236                       2606    943548 (   clinics_procedure clinics_procedure_pkey 
   CONSTRAINT     f   ALTER TABLE ONLY public.clinics_procedure
    ADD CONSTRAINT clinics_procedure_pkey PRIMARY KEY (id);
 R   ALTER TABLE ONLY public.clinics_procedure DROP CONSTRAINT clinics_procedure_pkey;
       public            postgres    false    234                       2606    943540 *   clinics_speciality clinics_speciality_pkey 
   CONSTRAINT     h   ALTER TABLE ONLY public.clinics_speciality
    ADD CONSTRAINT clinics_speciality_pkey PRIMARY KEY (id);
 T   ALTER TABLE ONLY public.clinics_speciality DROP CONSTRAINT clinics_speciality_pkey;
       public            postgres    false    232            �           2606    943408 &   django_admin_log django_admin_log_pkey 
   CONSTRAINT     d   ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);
 P   ALTER TABLE ONLY public.django_admin_log DROP CONSTRAINT django_admin_log_pkey;
       public            postgres    false    217            �           2606    943292 E   django_content_type django_content_type_app_label_model_76bd3d3b_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);
 o   ALTER TABLE ONLY public.django_content_type DROP CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq;
       public            postgres    false    203    203            �           2606    943290 ,   django_content_type django_content_type_pkey 
   CONSTRAINT     j   ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);
 V   ALTER TABLE ONLY public.django_content_type DROP CONSTRAINT django_content_type_pkey;
       public            postgres    false    203            �           2606    943282 (   django_migrations django_migrations_pkey 
   CONSTRAINT     f   ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);
 R   ALTER TABLE ONLY public.django_migrations DROP CONSTRAINT django_migrations_pkey;
       public            postgres    false    201            �           2606    943529 "   django_session django_session_pkey 
   CONSTRAINT     i   ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);
 L   ALTER TABLE ONLY public.django_session DROP CONSTRAINT django_session_pkey;
       public            postgres    false    230            �           2606    943507 .   patients_appointment patients_appointment_pkey 
   CONSTRAINT     l   ALTER TABLE ONLY public.patients_appointment
    ADD CONSTRAINT patients_appointment_pkey PRIMARY KEY (id);
 X   ALTER TABLE ONLY public.patients_appointment DROP CONSTRAINT patients_appointment_pkey;
       public            postgres    false    229            �           1259    943429    auth_group_name_a6ea08ec_like    INDEX     h   CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);
 1   DROP INDEX public.auth_group_name_a6ea08ec_like;
       public            postgres    false    207            �           1259    943366 (   auth_group_permissions_group_id_b120cbf9    INDEX     o   CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);
 <   DROP INDEX public.auth_group_permissions_group_id_b120cbf9;
       public            postgres    false    209            �           1259    943367 -   auth_group_permissions_permission_id_84c5c92e    INDEX     y   CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);
 A   DROP INDEX public.auth_group_permissions_permission_id_84c5c92e;
       public            postgres    false    209            �           1259    943352 (   auth_permission_content_type_id_2f476e4b    INDEX     o   CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);
 <   DROP INDEX public.auth_permission_content_type_id_2f476e4b;
       public            postgres    false    205            �           1259    943382 "   auth_user_groups_group_id_97559544    INDEX     c   CREATE INDEX auth_user_groups_group_id_97559544 ON public.auth_user_groups USING btree (group_id);
 6   DROP INDEX public.auth_user_groups_group_id_97559544;
       public            postgres    false    213            �           1259    943381 !   auth_user_groups_user_id_6a12ed8b    INDEX     a   CREATE INDEX auth_user_groups_user_id_6a12ed8b ON public.auth_user_groups USING btree (user_id);
 5   DROP INDEX public.auth_user_groups_user_id_6a12ed8b;
       public            postgres    false    213            �           1259    943396 1   auth_user_user_permissions_permission_id_1fbb5f2c    INDEX     �   CREATE INDEX auth_user_user_permissions_permission_id_1fbb5f2c ON public.auth_user_user_permissions USING btree (permission_id);
 E   DROP INDEX public.auth_user_user_permissions_permission_id_1fbb5f2c;
       public            postgres    false    215            �           1259    943395 +   auth_user_user_permissions_user_id_a95ead1b    INDEX     u   CREATE INDEX auth_user_user_permissions_user_id_a95ead1b ON public.auth_user_user_permissions USING btree (user_id);
 ?   DROP INDEX public.auth_user_user_permissions_user_id_a95ead1b;
       public            postgres    false    215            �           1259    943423     auth_user_username_6821ab7c_like    INDEX     n   CREATE INDEX auth_user_username_6821ab7c_like ON public.auth_user USING btree (username varchar_pattern_ops);
 4   DROP INDEX public.auth_user_username_6821ab7c_like;
       public            postgres    false    211            �           1259    943499 "   clinics_address_clinic_id_e0bcc24d    INDEX     c   CREATE INDEX clinics_address_clinic_id_e0bcc24d ON public.clinics_address USING btree (clinic_id);
 6   DROP INDEX public.clinics_address_clinic_id_e0bcc24d;
       public            postgres    false    227                       1259    943646 <   clinics_appointmentdoctort_appointmentdoctortime_id_a9c0f588    INDEX     �   CREATE INDEX clinics_appointmentdoctort_appointmentdoctortime_id_a9c0f588 ON public.clinics_appointmentdoctortime_times USING btree (appointmentdoctortime_id);
 P   DROP INDEX public.clinics_appointmentdoctort_appointmentdoctortime_id_a9c0f588;
       public            postgres    false    242                       1259    943633 0   clinics_appointmentdoctortime_doctor_id_4a1eca18    INDEX        CREATE INDEX clinics_appointmentdoctortime_doctor_id_4a1eca18 ON public.clinics_appointmentdoctortime USING btree (doctor_id);
 D   DROP INDEX public.clinics_appointmentdoctortime_doctor_id_4a1eca18;
       public            postgres    false    240                       1259    943647 ?   clinics_appointmentdoctortime_times_appointmenttime_id_2edb802f    INDEX     �   CREATE INDEX clinics_appointmentdoctortime_times_appointmenttime_id_2edb802f ON public.clinics_appointmentdoctortime_times USING btree (appointmenttime_id);
 S   DROP INDEX public.clinics_appointmentdoctortime_times_appointmenttime_id_2edb802f;
       public            postgres    false    242            �           1259    943481 "   clinics_clinic_changed_at_7f9300b6    INDEX     c   CREATE INDEX clinics_clinic_changed_at_7f9300b6 ON public.clinics_clinic USING btree (changed_at);
 6   DROP INDEX public.clinics_clinic_changed_at_7f9300b6;
       public            postgres    false    221            �           1259    943480 "   clinics_clinic_created_at_f052ebc7    INDEX     c   CREATE INDEX clinics_clinic_created_at_f052ebc7 ON public.clinics_clinic USING btree (created_at);
 6   DROP INDEX public.clinics_clinic_created_at_f052ebc7;
       public            postgres    false    221            �           1259    943610    clinics_clinic_user_id_08593ae6    INDEX     ]   CREATE INDEX clinics_clinic_user_id_08593ae6 ON public.clinics_clinic USING btree (user_id);
 3   DROP INDEX public.clinics_clinic_user_id_08593ae6;
       public            postgres    false    221            �           1259    943493 &   clinics_clinicphoto_clinic_id_b4217a26    INDEX     k   CREATE INDEX clinics_clinicphoto_clinic_id_b4217a26 ON public.clinics_clinicphoto USING btree (clinic_id);
 :   DROP INDEX public.clinics_clinicphoto_clinic_id_b4217a26;
       public            postgres    false    225            �           1259    943487 !   clinics_doctor_clinic_id_2ab40d3e    INDEX     a   CREATE INDEX clinics_doctor_clinic_id_2ab40d3e ON public.clinics_doctor USING btree (clinic_id);
 5   DROP INDEX public.clinics_doctor_clinic_id_2ab40d3e;
       public            postgres    false    223                       1259    943597 ,   clinics_doctor_procedures_doctor_id_26786e9b    INDEX     w   CREATE INDEX clinics_doctor_procedures_doctor_id_26786e9b ON public.clinics_doctor_procedures USING btree (doctor_id);
 @   DROP INDEX public.clinics_doctor_procedures_doctor_id_26786e9b;
       public            postgres    false    238                       1259    943598 /   clinics_doctor_procedures_procedure_id_0ebccdba    INDEX     }   CREATE INDEX clinics_doctor_procedures_procedure_id_0ebccdba ON public.clinics_doctor_procedures USING btree (procedure_id);
 C   DROP INDEX public.clinics_doctor_procedures_procedure_id_0ebccdba;
       public            postgres    false    238                       1259    943575 .   clinics_doctor_specialities_doctor_id_a4490204    INDEX     {   CREATE INDEX clinics_doctor_specialities_doctor_id_a4490204 ON public.clinics_doctor_specialities USING btree (doctor_id);
 B   DROP INDEX public.clinics_doctor_specialities_doctor_id_a4490204;
       public            postgres    false    236                       1259    943576 2   clinics_doctor_specialities_speciality_id_86f10774    INDEX     �   CREATE INDEX clinics_doctor_specialities_speciality_id_86f10774 ON public.clinics_doctor_specialities USING btree (speciality_id);
 F   DROP INDEX public.clinics_doctor_specialities_speciality_id_86f10774;
       public            postgres    false    236                       1259    943554 $   clinics_procedure_parent_id_14e46f96    INDEX     g   CREATE INDEX clinics_procedure_parent_id_14e46f96 ON public.clinics_procedure USING btree (parent_id);
 8   DROP INDEX public.clinics_procedure_parent_id_14e46f96;
       public            postgres    false    234            �           1259    943419 )   django_admin_log_content_type_id_c4bce8eb    INDEX     q   CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);
 =   DROP INDEX public.django_admin_log_content_type_id_c4bce8eb;
       public            postgres    false    217            �           1259    943420 !   django_admin_log_user_id_c564eba6    INDEX     a   CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);
 5   DROP INDEX public.django_admin_log_user_id_c564eba6;
       public            postgres    false    217            �           1259    943531 #   django_session_expire_date_a5c62663    INDEX     e   CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);
 7   DROP INDEX public.django_session_expire_date_a5c62663;
       public            postgres    false    230                        1259    943530 (   django_session_session_key_c0390e0f_like    INDEX     ~   CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);
 <   DROP INDEX public.django_session_session_key_c0390e0f_like;
       public            postgres    false    230            �           1259    943520 1   patients_appointment_appointment_time_id_c69fcc3f    INDEX     �   CREATE INDEX patients_appointment_appointment_time_id_c69fcc3f ON public.patients_appointment USING btree (appointment_time_id);
 E   DROP INDEX public.patients_appointment_appointment_time_id_c69fcc3f;
       public            postgres    false    229            �           1259    943519 (   patients_appointment_changed_at_53d5b0ba    INDEX     o   CREATE INDEX patients_appointment_changed_at_53d5b0ba ON public.patients_appointment USING btree (changed_at);
 <   DROP INDEX public.patients_appointment_changed_at_53d5b0ba;
       public            postgres    false    229            �           1259    943518 (   patients_appointment_created_at_e644a685    INDEX     o   CREATE INDEX patients_appointment_created_at_e644a685 ON public.patients_appointment USING btree (created_at);
 <   DROP INDEX public.patients_appointment_created_at_e644a685;
       public            postgres    false    229            �           1259    943521 '   patients_appointment_doctor_id_ff42f56c    INDEX     m   CREATE INDEX patients_appointment_doctor_id_ff42f56c ON public.patients_appointment USING btree (doctor_id);
 ;   DROP INDEX public.patients_appointment_doctor_id_ff42f56c;
       public            postgres    false    229                       2606    943361 O   auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;
 y   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm;
       public          postgres    false    205    209    3014                       2606    943356 P   auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;
 z   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id;
       public          postgres    false    3019    209    207                       2606    943347 E   auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;
 o   ALTER TABLE ONLY public.auth_permission DROP CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co;
       public          postgres    false    203    3009    205            !           2606    943376 D   auth_user_groups auth_user_groups_group_id_97559544_fk_auth_group_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;
 n   ALTER TABLE ONLY public.auth_user_groups DROP CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id;
       public          postgres    false    207    213    3019                        2606    943371 B   auth_user_groups auth_user_groups_user_id_6a12ed8b_fk_auth_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;
 l   ALTER TABLE ONLY public.auth_user_groups DROP CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id;
       public          postgres    false    3027    211    213            #           2606    943390 S   auth_user_user_permissions auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;
 }   ALTER TABLE ONLY public.auth_user_user_permissions DROP CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm;
       public          postgres    false    205    215    3014            "           2606    943385 V   auth_user_user_permissions auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public.auth_user_user_permissions DROP CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id;
       public          postgres    false    215    3027    211            )           2606    943494 G   clinics_address clinics_address_clinic_id_e0bcc24d_fk_clinics_clinic_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.clinics_address
    ADD CONSTRAINT clinics_address_clinic_id_e0bcc24d_fk_clinics_clinic_id FOREIGN KEY (clinic_id) REFERENCES public.clinics_clinic(id) DEFERRABLE INITIALLY DEFERRED;
 q   ALTER TABLE ONLY public.clinics_address DROP CONSTRAINT clinics_address_clinic_id_e0bcc24d_fk_clinics_clinic_id;
       public          postgres    false    227    221    3052            2           2606    943636 c   clinics_appointmentdoctortime_times clinics_appointmentd_appointmentdoctortim_a9c0f588_fk_clinics_a    FK CONSTRAINT     	  ALTER TABLE ONLY public.clinics_appointmentdoctortime_times
    ADD CONSTRAINT clinics_appointmentd_appointmentdoctortim_a9c0f588_fk_clinics_a FOREIGN KEY (appointmentdoctortime_id) REFERENCES public.clinics_appointmentdoctortime(id) DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public.clinics_appointmentdoctortime_times DROP CONSTRAINT clinics_appointmentd_appointmentdoctortim_a9c0f588_fk_clinics_a;
       public          postgres    false    240    3094    242            3           2606    943641 a   clinics_appointmentdoctortime_times clinics_appointmentd_appointmenttime_id_2edb802f_fk_clinics_a    FK CONSTRAINT     �   ALTER TABLE ONLY public.clinics_appointmentdoctortime_times
    ADD CONSTRAINT clinics_appointmentd_appointmenttime_id_2edb802f_fk_clinics_a FOREIGN KEY (appointmenttime_id) REFERENCES public.clinics_appointmenttime(id) DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public.clinics_appointmentdoctortime_times DROP CONSTRAINT clinics_appointmentd_appointmenttime_id_2edb802f_fk_clinics_a;
       public          postgres    false    219    242    3048            1           2606    943628 R   clinics_appointmentdoctortime clinics_appointmentd_doctor_id_4a1eca18_fk_clinics_d    FK CONSTRAINT     �   ALTER TABLE ONLY public.clinics_appointmentdoctortime
    ADD CONSTRAINT clinics_appointmentd_doctor_id_4a1eca18_fk_clinics_d FOREIGN KEY (doctor_id) REFERENCES public.clinics_doctor(id) DEFERRABLE INITIALLY DEFERRED;
 |   ALTER TABLE ONLY public.clinics_appointmentdoctortime DROP CONSTRAINT clinics_appointmentd_doctor_id_4a1eca18_fk_clinics_d;
       public          postgres    false    240    223    3056            &           2606    943605 >   clinics_clinic clinics_clinic_user_id_08593ae6_fk_auth_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.clinics_clinic
    ADD CONSTRAINT clinics_clinic_user_id_08593ae6_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;
 h   ALTER TABLE ONLY public.clinics_clinic DROP CONSTRAINT clinics_clinic_user_id_08593ae6_fk_auth_user_id;
       public          postgres    false    211    3027    221            (           2606    943488 O   clinics_clinicphoto clinics_clinicphoto_clinic_id_b4217a26_fk_clinics_clinic_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.clinics_clinicphoto
    ADD CONSTRAINT clinics_clinicphoto_clinic_id_b4217a26_fk_clinics_clinic_id FOREIGN KEY (clinic_id) REFERENCES public.clinics_clinic(id) DEFERRABLE INITIALLY DEFERRED;
 y   ALTER TABLE ONLY public.clinics_clinicphoto DROP CONSTRAINT clinics_clinicphoto_clinic_id_b4217a26_fk_clinics_clinic_id;
       public          postgres    false    225    221    3052            '           2606    943482 E   clinics_doctor clinics_doctor_clinic_id_2ab40d3e_fk_clinics_clinic_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.clinics_doctor
    ADD CONSTRAINT clinics_doctor_clinic_id_2ab40d3e_fk_clinics_clinic_id FOREIGN KEY (clinic_id) REFERENCES public.clinics_clinic(id) DEFERRABLE INITIALLY DEFERRED;
 o   ALTER TABLE ONLY public.clinics_doctor DROP CONSTRAINT clinics_doctor_clinic_id_2ab40d3e_fk_clinics_clinic_id;
       public          postgres    false    3052    221    223            /           2606    943587 N   clinics_doctor_procedures clinics_doctor_proce_doctor_id_26786e9b_fk_clinics_d    FK CONSTRAINT     �   ALTER TABLE ONLY public.clinics_doctor_procedures
    ADD CONSTRAINT clinics_doctor_proce_doctor_id_26786e9b_fk_clinics_d FOREIGN KEY (doctor_id) REFERENCES public.clinics_doctor(id) DEFERRABLE INITIALLY DEFERRED;
 x   ALTER TABLE ONLY public.clinics_doctor_procedures DROP CONSTRAINT clinics_doctor_proce_doctor_id_26786e9b_fk_clinics_d;
       public          postgres    false    238    223    3056            0           2606    943592 Q   clinics_doctor_procedures clinics_doctor_proce_procedure_id_0ebccdba_fk_clinics_p    FK CONSTRAINT     �   ALTER TABLE ONLY public.clinics_doctor_procedures
    ADD CONSTRAINT clinics_doctor_proce_procedure_id_0ebccdba_fk_clinics_p FOREIGN KEY (procedure_id) REFERENCES public.clinics_procedure(id) DEFERRABLE INITIALLY DEFERRED;
 {   ALTER TABLE ONLY public.clinics_doctor_procedures DROP CONSTRAINT clinics_doctor_proce_procedure_id_0ebccdba_fk_clinics_p;
       public          postgres    false    3077    234    238            -           2606    943565 P   clinics_doctor_specialities clinics_doctor_speci_doctor_id_a4490204_fk_clinics_d    FK CONSTRAINT     �   ALTER TABLE ONLY public.clinics_doctor_specialities
    ADD CONSTRAINT clinics_doctor_speci_doctor_id_a4490204_fk_clinics_d FOREIGN KEY (doctor_id) REFERENCES public.clinics_doctor(id) DEFERRABLE INITIALLY DEFERRED;
 z   ALTER TABLE ONLY public.clinics_doctor_specialities DROP CONSTRAINT clinics_doctor_speci_doctor_id_a4490204_fk_clinics_d;
       public          postgres    false    223    3056    236            .           2606    943570 T   clinics_doctor_specialities clinics_doctor_speci_speciality_id_86f10774_fk_clinics_s    FK CONSTRAINT     �   ALTER TABLE ONLY public.clinics_doctor_specialities
    ADD CONSTRAINT clinics_doctor_speci_speciality_id_86f10774_fk_clinics_s FOREIGN KEY (speciality_id) REFERENCES public.clinics_speciality(id) DEFERRABLE INITIALLY DEFERRED;
 ~   ALTER TABLE ONLY public.clinics_doctor_specialities DROP CONSTRAINT clinics_doctor_speci_speciality_id_86f10774_fk_clinics_s;
       public          postgres    false    236    232    3074            ,           2606    943599 N   clinics_procedure clinics_procedure_parent_id_14e46f96_fk_clinics_procedure_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.clinics_procedure
    ADD CONSTRAINT clinics_procedure_parent_id_14e46f96_fk_clinics_procedure_id FOREIGN KEY (parent_id) REFERENCES public.clinics_procedure(id) DEFERRABLE INITIALLY DEFERRED;
 x   ALTER TABLE ONLY public.clinics_procedure DROP CONSTRAINT clinics_procedure_parent_id_14e46f96_fk_clinics_procedure_id;
       public          postgres    false    3077    234    234            $           2606    943409 G   django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co    FK CONSTRAINT     �   ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;
 q   ALTER TABLE ONLY public.django_admin_log DROP CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co;
       public          postgres    false    217    203    3009            %           2606    943414 B   django_admin_log django_admin_log_user_id_c564eba6_fk_auth_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;
 l   ALTER TABLE ONLY public.django_admin_log DROP CONSTRAINT django_admin_log_user_id_c564eba6_fk_auth_user_id;
       public          postgres    false    211    3027    217            *           2606    943508 S   patients_appointment patients_appointment_appointment_time_id_c69fcc3f_fk_clinics_a    FK CONSTRAINT     �   ALTER TABLE ONLY public.patients_appointment
    ADD CONSTRAINT patients_appointment_appointment_time_id_c69fcc3f_fk_clinics_a FOREIGN KEY (appointment_time_id) REFERENCES public.clinics_appointmenttime(id) DEFERRABLE INITIALLY DEFERRED;
 }   ALTER TABLE ONLY public.patients_appointment DROP CONSTRAINT patients_appointment_appointment_time_id_c69fcc3f_fk_clinics_a;
       public          postgres    false    219    229    3048            +           2606    943513 Q   patients_appointment patients_appointment_doctor_id_ff42f56c_fk_clinics_doctor_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.patients_appointment
    ADD CONSTRAINT patients_appointment_doctor_id_ff42f56c_fk_clinics_doctor_id FOREIGN KEY (doctor_id) REFERENCES public.clinics_doctor(id) DEFERRABLE INITIALLY DEFERRED;
 {   ALTER TABLE ONLY public.patients_appointment DROP CONSTRAINT patients_appointment_doctor_id_ff42f56c_fk_clinics_doctor_id;
       public          postgres    false    223    229    3056            �      x�3�L����L.����� #<�      �   <   x����0��s<L�$�]���ӓ,ٖ�;>1n��X�75�=�l,4��|��
_      �   �  x���͊�0���S�	J������1$�q����L��,J)�)�>@��6�
�U���{�`�,l�;ґ}�d��.3o�Zy�|�%YU�2���{u�o����f��B�&\%����ir`��i�`M����Y���t�K��ښk�Sl����3쏰`�sg���#���u��h����	6g�� {���wV,�]@w�:���@s�E��^�� � �� S77t�M笝9γJ�5��-i�Դp1�F:0"������������.aE�z���:Ն����>[�T���^��Zw�v�"�����N��_��'Ϟ�;z�Y���V6�F�E��Y�mV�nՊHF��u�F!����ft�z#�D��I�J,��M]m�,�y@��#mQLRփmE���CM9�'�ɋ|�䥾c�s��U^�d�ÁK��4vP�hQ���Z�%T�V����Bܒ�L�Q�7y��u@H2hIr��m�R<�D� t.����]}τ9�ԯT9�!I5�l",J�MQ[�E馠�m����G�,��}}�EB�݀�{D��6i�G�ǚ�8�#�n�y���K)O�gE�S}P��>0aN�]���r�V����ڍ�i��v�Fj�j�6��hG����E	O�*>��#�h.�<NV�2���*�W��]��~�8�/�J�w��^z&��[�f�ћy4��$�+��[��ѕZF�M'/>�Dԫk4л7���Bt��      �   �   x�m�KO�@����+�`�����V��ML��Z�S��녅;�پ��&��_)�B���(˨�Μ��x,��-k���K���wN�����{Xݚ���H5��I�-����kD����6X6f5���jQ�vjW�~m���	H��M��"�Z��L�}���7OI����u���d�d?�|�,:v�Jko���������'��a20,I��Y��Sٮabs��|o��idT�      �      x�3�4�4����� �[      �      x������ � �      �   �   x�}���@D��*.�B�P����v�*� d�j����r����ir�"V�tp�#f�${�iK�BꯕO���#Z�M�~q������Rd{���������1cD0Py
z2�@��6���ϠB�LD
ʀ�      �   Y   x�U��� C�s�IJ�]��5���'K_�}ywo=������V��^^�e���=CN��K{�֞av�q7�ҵG���G{��_�|�V(X      �   �   x���@߸�hw�{I�u��k�XBP���E����G�D�5�W~EG1�}?��E�����D�-��1����<10.&&�'p.�s�N���yM'a���k������Zl������>��m�~Dz�s�s�UH��7� 
�����J!Z��� ���3       �   �   x�=��m�@Cѵ\L����Ԓ����|�g#p�����D�'�<��<z�'u!�>�E�ȣ�yS�ч#�oy��sq�M���|��su�7�>w_�q�����D��BK����B[s�鏅��F�_�-G�!��V��sW{�����������������������ۉ�����6�~[jo/4�������?�u�Q�b�      �   �  x��VMoU];����Lf���mlK6���T�8
a��	n吠6�T�v4�=x�-����%�{�3v�K�y�~�{νS��Ba7,�F�&���k�b%���R�^Xξ-���~=�(��ղ��W��+aX)�ð���ؙM];�ٗ�omj�e'�,,ۮi���y�������؅k�7qmc��~o�8�Nϸ�
������W����N*�&��x���ؗ���a�~䬱�..���=�H]7���\kb{�g��ss;�ݐs���!ӄ~�H�'ν�஄�n^,�r�R,�3>u؍��f6q^ւςV�:A��v�y�OW8N����."4䍣0m] r�w���KXC�9898�������H�&F£�[S�b���(ӓ̉6����I�̮T���������-Ln��3�z�.$��i�P�ΌD:��ܕ��L^�3:=6��ezA'���3��]%Ӣ��!x��NVإ�B鋁.���u%�	)(Ĝ�����������&��`HH �Z�"��pZ�o����c���r� �[���{,�X�%U�6R��:�_������o�������}�q�������0�W��H���(�K�L��[���RU��fpS�/�&}�@���,R����|d�8ca�[h3WVX�{_}VFt<d ��:(��l!�2��MF�L��C��X��)�G���R~���O%ک����5!¸�ꆡI'���M�#�!��/'�׌Bk2,n����1�G�|m=��o�P��.��	QU��l��Rܑ����=S��0O�3l�-�t��_���D@v�,�L��h�<{Ya�wǙb�B��Yn�z�����60��]��}'�}i���W��])�=%��K�҇������]p\�P�Ka���l8*�0mthuN�Hvh�2�
)}�*����$�G�S�����s�;q�RH��#~�ϼN�Պ�d(�:]%�9tP)��c�b$���=�DWsNY��o-U�Jb�'��0�W��,|�e���������DG�Z��[��Xi�/V�҄۟8��Tרd�v�;zQ^�����d'&�ݩ�e� ��j�?Q3uY�*Q�K|R��.������W{?:z�`�����q���ap|�0�Nw���a�O�">�r�V�/n|=�LՋ���J�Z,���R	�ժ�ps���'����'_�?ˑ4)[��m����N���7�����������Q9���� �1��      �      x������ � �      �   �   x�}�=
�@���a�ݍ�BDP[A$���D����F��gx�r��XX�{��y���F��f,8!���Cb�l.�c��	�*�e���(l����:A7��D���N�˅z֕�6-IX>7f́	n��A���}�ǜǑQ�G���R9Wʓ˰I���7I:U���݈O��Ms	+\S4a��k�iM?%�F����]�-�z�χ�      �   *   x�3�4�4�2��\Ɯ@�˄�H�Ic.3 i����� gX�      �   -   x�Ź  ��[�y���:p"Y�q0�Y��x���I�k��@�      �   ~   x�-���@Ek{�� ������U*�HE��DVx��Ka���-���H��h;�{�RW�ѕp���F^>�ގ�V
g.��5v����3��d6I��z��M������ctp��f{�P���Y      �   �   x�u�]
�0����T����ô��A��c0��^a�FΪ	(Hd���ݔg�d+��|��4�|�x��"���QݩP�! R�pG���L=�]�s�Wo��1��U����<�DZ�)�b�b 2\鏯m,�'f�\��?͎R�g�fd�}�Ŭ      �   �  x��\[k%�~>���b]U}=ρ<����f�.G�{�H�'c��I��	$&b�c@���E�_9(��=����9�Vl��ё�������]}`�qK�-��ps�9�Zj�B�H�̄��_�V��ɿ�w_{{s{oo��9��~�{33�,���I:��c��X`�(Ǣ9��%�r�������b���g���(���(�"P�?��o���ۜ6g�w7'���Y�������U�?��oN����_�<��CT�9��F�L�`���sV]�B (%��ԃ
Ȱ:���_�2�T�0Aټ���_l����� �o$�o2���O��J��`�7�݇$�?٩�`'�÷��E��H�a����+�T��G�o����y)��7��5���#����������<;�]�'}f�o����up�*�^~��]V@�FJ�4q1*�+�6y���,�K߼ԷKT���
k�-j/+|�Ys�/N�o�W���?� r\��(�rb
A������_�5�?X��w�/_�����l��D��-R��K��[�݃�7,�6�u~  �y�d%i-�Ө�;�v����eJfD�ɟ� �_G�LFPsԵD���W!S�����˪�'z�?��s}6�p/��a�(&�`�i��z�p�_J9/b�}L�v1�*�v�	�u"\�3�q܅PK+C�� �X����	78��I(�V�t���e�������V���`r��׹�v����������dBr>��aY���6��¹R��Z�}旦
zN����9�6��;��N~��:;�����Vͷ<����K?������=�scaj��`�C�<i�4g�k�?�d�N�n��Z���U��E���br����Q�g������|����Dj�R���QQ,�~���5�|��[k+�k:͚G��/��6_�'����λ�Zâ{89k>m>���l<�Яk�%�L K<.KpE�&��)*�?��~���OU��x�/O�Un���h% =gB�����b��p9��ԩ����5����o�?�=ꙁO��� �k�3�|���m��V6�>j2\F�d���~r����8��娭Z�S�n�J�v �|��W�e\0��i����pn��_g�9�k]�a��������������e�3���9�ڐFR�*�70�e�?{�b�T�X�f9���\`tQ;=����>�����N-d�Z��J�Dw���v�d�x�;#�F�8�R'��bP-��7���Q�4�\q�,k-Ht>����J������`��q�'�I������N���ޭ?;�}�a�O?���8��|^����4�GN��R���47����l6;�ڤ��&������R���^�'©tܒE�RTΫ%(Rv��_��R�J�#����
��v�c/
�.�h)�3
���\��.�g;��7��܏�k����� ��ӟ�)H����T����b�**��~���{ �E�MRfӓ<C��/vi�_8G�L�9�.NZw�Bys3��+h�z*��^�Rr]x8�}�߷��p���MUgؾ�5I�B��3pBl	��õ�F�L�|���kc�d�-/���Sh����ʆڀ���Ӭ=�8�S���F1UCE'<{��C�p[�sI58�l,#��h�&A�~6���	!е��̸�~�̇���\n�nӒ0� ���r��n��*7��B�d&��ځ*%�@s��@u<�y}�ܖ;PcMHk����#���GZTvA���v8�`C ���>L -XA��bF1��NErp@e�;[��(=�(ˌj1'J�v��	����چ��@(=@�K�	���bH��	�2��lPa�&��uӟ@(3@(B���	�2�r!���'3�'G���6�69�@���>� �.0'���ɩ��1�Jf�JΈ�hM`�`�3.n�ix����ژ4r�ͳg�{%̔E�s�9�ZY���Q %{*K(ˀ.�~@<��U �%� $
�!�+ �K@5 (Ehːb@}	� U�!�
���3W��5����2k.� �:7���ĉ� �zK�` �Ś��zk�r���-�9�P<���y�[Pl�8{q]�W?�UmB��4���<�U�������w8��W�WOT��&t�s��-^v��;�^�n͝n�M��N�צ�޶��m�py���w�:Nד���6�_���X��Y��6�Ű����YZ�l���n�n�2��jO��W��o�Vo`_��6��m�,ׯ���4}��ޔ���қ���R9��sm���(��T߳}�����p�b�;`֟��;W�í���B��Ct��>��B�x�� ��% �N!%��G<B�I�= �&�ϝ|���x*�K�-K�i��c� [[+ ޥ�`DU(֡f���fD��j+Pk�3`D��>[��2/���o�(���~/'|3Y<�e�	
;4�b�V`��,6D7"�hB7�ҡ��� 
C4��z�f0r�0D��\���1����D��hkTla�� �h��1c�ְd:��ȋ��&��5��HK@a��Q�ث!gm7�
��#�Y�g�8�k���C�����V�L
J��Z_c������3)�i�g ���a��XԂ��[�mc
��H�`�M�c�!�\촂�XP�� �Ȱ{���� 5��Elw���RXP����څ���X���w���'������wf5j���+b�0����k�@K�H�`,La���{^vÄ�0��!:�	d����|����}��}�2�G�X����U �QƱ-�RS�["�`Kd�C<���0E�%z [��	H1��0E�%�M�5(���SmS�[�е6�)�}�c���Z�X��}��X���@:��6^e���#M�@�%2��G*���]x,�Qn�~<Gj".�<�)7D?_���b�h�)x�#����u�)L�z�a	dj���z5�Y(յ�<j�:���C�e���lΚ��NK{�s��>$�Мi:|n���_��Z�1"W�Q��~C����;��X��gy���^#�u�^5=mop^��r̶�[g����j�A�N����}��t�0v ���b��<�뛫�L��5�9Df7k>n7�OWQ�-�jp��O��	O���^�Cs?C�JhWB�ۧ�����✮�Ŭk����U'ih�ӄ���m�q�vn^£��#���_���6ӯ]�w��׮��}K����,����⴩�-�i����ܘ�Ory�������ee      �   �   x�mNI�0<{�;�%Xjc+q�=�������l�b�P�W.^Gl(~#��Kk���V��W�)i�I�q�<p��Ou{-8R�Hj�T������'��5�V���n�ޞ9�)aC]&���Bm�Ib'>"�Ԫ&�Ce����s�g��
���l�      �   C  x���ۮ�8E�s���G�\廿e$w�5ܚ˙�ߏ/	19�$/�(o�] �f��/�yt���~�u{@������~mP�*�%Q�/">�P����
�@+�>v�]"�$���Jж�)4:������������F����7�1B��������'�|�	
<dh-"K|���\n�x��u���j�Ԑ�~h�vq����y�-�z��l��Sx�!��1�Ԇ��:���j߾��)z�����a\���XZ���KB[�Kއu��-�Dfl����i�6�n�bOD�&��S^:��[��a��ֻi&۹y�O�v�k�pté�Ҽ�X2����6��&�[(E����W��4��&FP�Fl��$rv��?�O��D��ؼX�ꗟ�]�VTf�:4m��Hr�:�c����wʤB�g9����e�
���P�x]r��(�L���!ji��zj��5�~9G�w\��!�pUq�*�i�`�84��7�ߛ:�a�
��$/��~%��C��iE��� 3H*������='�w n# �␥%@n�WY�7[�PRQ$Tf�,�ꮵ7���&l-7*��R�p�`}c[?_��������L]@��F	�8��꺔�G"1H*�$�lJJ6��A�����GИ�l r��2�4��q������$5��I2�iE�	Z�������@K'O�4�5�?����-3�{�Y��\{�{uv	�˧�vd^1@vQ����%��; %0�̭���k�nκsC0Z���z BÁ��_���!���_�w����w�f���+���������J      �   j  x���Y��F @��׫���(���?l0��<�"!�y�`{�i�$Jz	���{s��Y6b3sI��O
�S�sW�ZD����sΤ�3��V��Ф��.�.�l��;���m��}k�H��[%������$��ZX�F��b�g��EP�nW��9��9��;u��J�����)�^ώ<���!�u�M����6fu�5J�Fu�ٟE�wU/�RU3 �U�8)5��(Lh���b�jk�֙���!���H߁ r@��c,`�����-�qV��P�a��좬Ȃ���#�X�Q�G���bG�d��*�%�!�ֹ��i[͗�7#��0]�"�����d;oȽ,��"���L����{6���L#�ى�'$��X̍�t����1=s�릤�ݑ`tw�j�^�3�Y*"b��0! ���"{��&Y\z���H_����G�Ў��,�lW��M>�+�K��-�ރ��Y�XЖ���)��"�_F `��QK'�|��>�&�'B�'4��L����)��F����ܔr�B�>�Z��I:�݉F�k�)t�8��R����qc�.��F��i[��dZЍ|W����1�}�;Wĵ��2v��?؟��=+S}�O �[�yzU4�ՄZL�d��lة/l�u9��!�2�N�Yd\̮>�S9$;��^-_��&l�aqs|<"�F�V��w�ˈ�,��!�������-� _E��X�~Q��-���G�Fڈݜ�a����p��lvO��z���z�r�i/gS�÷�8!� ��߯5i>�{Y�	�,��c�&3��Bh��g��orѯ;��"���G!Y���}гz�xE�� �A�fċ�+%� �����x{{�|��2      �   H   x��ɱ�0�ڞ�%�w�2�1�g��\{�@D�֨��B�TJ+�������5 d&��0������#     