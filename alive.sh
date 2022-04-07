echo "-- KEEP SERVER ALIVE --"
count=1
SERVER_URL="https://yts-api.herokuapp.com/"
while true ; 
    do 
        if [[ ! -v SERVER_URL ]]; then
            echo "[ ERROR ] SERVER_URL is not set"
        elif [[ -z "$SERVER_URL" ]]; then
            echo "[ ERROR ] SERVER_URL is set to the empty string"
        else
            x=$(curl -s $SERVER_URL); 
            echo "[ INFO ] Ping SERVER - $count -  : $SERVER_URL"
            count=$(($count+1))
        fi
        sleep 600 ; 
        
done