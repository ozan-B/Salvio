#!/bin/bash

# ipinfo.io'dan bilgileri al
ip_info=$(curl -s ipinfo.io)

# "ip" alanını al
ip_value=$(echo "$ip_info" | jq -r '.ip')
city_value=$(echo "$ip_info" | jq -r '.city')
country_value=$(echo "$ip_info" | jq -r '.country')
loc_value=$(echo "$ip_info" | jq -r '.loc')
timezone_value=$(echo "$ip_info" | jq -r '.timezone')

# Kırmızı renkte yazdırma fonksiyonu
print_red() {
  echo -e "\e[31m$1\e[0m"
}

# "ip" değerini kırmızı renkte yazdır
print_red "IP      : $ip_value"
print_red "City    : $city_value"
print_red "Country : $country_value"
print_red "Loc     : $loc_value"
print_red "Timezone: $timezone_value"
