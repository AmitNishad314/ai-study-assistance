import { useState } from "react";

export default function useLocalStorage(key, initialValue) {

    const [value, setValue] = useState(() => {
        try {
            const saved = localStorage.getItem(key);

            if (!saved || saved === "undefined") {
                return initialValue;
            }

            return JSON.parse(saved);
        } catch (err) {
            console.error("Invalid localStorage value:", err);
            return initialValue;
        }
    });

    function save(newValue) {

        setValue(prev => {
    
            const valueToStore =
                newValue instanceof Function
                    ? newValue(prev)
                    : newValue;
    
            localStorage.setItem(
                key,
                JSON.stringify(valueToStore)
            );
    
            return valueToStore;
        });
    
    }

    return [value, save];
}