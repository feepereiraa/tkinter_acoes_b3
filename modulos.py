import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from forex_python.converter import CurrencyRates
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import pandas as pd
import os
import time
import ccxt
