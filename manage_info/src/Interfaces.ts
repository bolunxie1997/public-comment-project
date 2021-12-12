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
interface UserItem {
    id: string|number;
    username: string;
    age: number;
    gender: string;
    type:number | string,
    ctime:string | Date
  }


export {
    FileInfo,
    FileItem,
    FormState,
    UserItem
}


