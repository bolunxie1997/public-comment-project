interface FileItem {
    uid: string;
    name?: string;
    status?: string;
    response?: string;
    percent?: number;
    url?: string;
    preview?: string;
    originFileObj?: any;
}

interface FileInfo {
    file: FileItem;
    fileList: FileItem[];
}


interface FormState {
    pass: string;
    checkPass: string;
    username:String,
    age: number | undefined;
}

export {
    FileInfo,
    FileItem,
    FormState
}


