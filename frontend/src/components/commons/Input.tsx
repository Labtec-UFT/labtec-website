import {useId, useState} from "react";
import type { InputHTMLAttributes } from "react";

type InputProps = {
    label: string;
} & InputHTMLAttributes<HTMLInputElement>;

export default function Input({ label, id, value: valueProp, onChange, ...rest }: InputProps) {
    const generatedId = useId();
    const inputId = id ?? generatedId;

    const isControlled = valueProp !== undefined;
    const [internalValue, setInternalValue] = useState("");

    const value = isControlled ? valueProp : internalValue;

    function handleChange(e: React.ChangeEvent<HTMLInputElement>) {
        if (!isControlled) {
            setInternalValue(e.target.value);
        }
        onChange?.(e);
    }

    return (
        <div className="relative w-fit">
            <label
                htmlFor={inputId}
                className="absolute left-3 -top-2 z-10 bg-white px-1 text-sm text-gray-900 dark:bg-zinc-950 dark:text-white whitespace-nowrap"
            >
                {label}
            </label>

            <input
                id={inputId}
                value={value}
                onChange={handleChange}
                {...rest}
                className="w-85 rounded-lg border-2 border-gray-300 px-3 py-2 bg-transparent focus:outline-none focus:ring-2 focus:ring-gray-700"
            />
        </div>
    );
}
