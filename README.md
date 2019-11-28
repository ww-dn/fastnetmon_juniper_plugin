# fastnetmon_juniper_plugin
Управление маршрутами juniper при срабатывании собития ban, unban в fastnetmon

**Скрипт использует python библиотеку для удаленного управления JunOS - py-junos-eznc. Подробное описание библиотеки: https://github.com/Juniper/py-junos-eznc**

### Установка
- устанавливаем зависимости, смотрим таблицу 1:  https://www.juniper.net/documentation/en_US/junos-pyez/topics/task/installation/junos-pyez-server-installing.html
- `sudo pip install junos-eznc`
- копируем файлы скриптов и кладем их в `/usr/local/bin`
- в строке файлов вписываем свои параметры:
`dev = Device(host='HOSTNAME', port='PORT', user='LOGIN', passwd='PASSWORD').open()`
- редактируем свой файл **notify_about_attack.sh** и приводим блоки ban, unban к такому виду:

```bash
if [ "$4" = "unban" ]; then
    /usr/bin/python3 /usr/local/bin/unban.py $1
    exit 0
fi

if [ "$4" = "ban" ]; then
    cat | mail -s "FastNetMon Guard: IP $1 blocked because $2 attack with power $3 pps" $email_notify;
    /usr/bin/python3 /usr/local/bin/ban.py $1
    exit 0
fi

```
