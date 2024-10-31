document.addEventListener("DOMContentLoaded", () => {
    // const download = document.querySelector("#download");
    // const process = document.querySelector("#process");
    // const output = document.querySelector(".output_pdf");
    const upload = document.querySelector("#upload_file");
    const fileform = document.querySelector("#fileForm");
    const pdfFrame = document.querySelector("#pdfFrame");
    const alertText = document.querySelector(".alertText");
    const loader = document.querySelector(".loader");
    const xhaxha = document.querySelector(".xhaxha");
    const modal_update = document.querySelector(".modal_update");
    const modal_fill_frame = document.querySelectorAll(".modal_item .fill_frame");
    const upload_files = document.querySelectorAll("input[type='file']");
    // const upload_excel = document.querySelector("#upload_excel");
    // const upload_img = document.querySelector("#upload_img");
    const URL = "http://127.0.0.1:8000/run_convert";
    let status = 0;
    // 0 無資料夾 
    // 1 loading 
    // 2 done
    xhaxha.addEventListener("click", () => {
        modal_update.classList.add("frame_none");
    })
    upload_files.forEach((element, index) => {
        element.addEventListener("change", (e) => {
            const file = e.target.files;
            FrameChange(file, index);
            // console.log(element, index);
            console.log(file, index);
            // console.log(file[0].webkitRelativePath.split("/")[0]);
        })
    });
    modal_fill_frame.forEach((element, index) => {
        element.addEventListener("click", (e) => {
            const bool = confirm("您確定要刪除檔案(資料夾)嗎？");
            if(bool){
                modal_fill_frame[index].classList.add("frame_none");
                upload_files[index].value = "";
                setTimeout(() => {
                    upload_files[index].disabled = false;
                }, 500);
            }
            else{
                e.preventDefault();
            }
            
        })
    });


    // upload part //
    upload.addEventListener("click", (event) => {
        modal_update.classList.remove("frame_none");
        // if (pdfFrame.src != "") {
        //     const bool = confirm('你確定要上傳資料夾嗎 (一但確認先前的資料夾不會復原！)');
        //     if (!bool) {
        //         event.preventDefault();
        //     }
        //     else {
        //         pdfFrame.src = "";
        //     }
        // }
    })

    // execute part //
    fileform.addEventListener('submit', (event) => {
        // pdfFrame.src = "";
        event.preventDefault();
        const getForm = new FormData(fileform);

        // single part 
        const ExcelData = upload_files[0].files[0];
        if(ExcelData){
            getForm.append('ExcelData',ExcelData);
        }

        // folder part 
        const Folder = upload_files[1].files; // 獲取資料夾中的所有檔案
        for (let i = 0; i < Folder.length; i++) {
            getForm.append('folderFiles[]', Folder[i]); // 將每個檔案添加到 FormData
        }

        for (let [key, value] of getForm.entries()) {
            console.log(key, value); // 這會顯示每個鍵和值
        }
        console.log(upload_files[0].files.length,Folder.length)
        if (Folder.length > 0 && upload_files[0].files.length > 0 ) {
            modal_update.classList.add("frame_none");
            StateAction(1);
            fetch(URL, {
                method: "POST",
                body: getForm
            })
                .then(res => {
                    if (!res.ok) {
                        console.log('res', res);
                    }
                })
                .then(data => {
                    console.log("data", data);
                    StateAction(2);
                    getData(data);
                })
                .catch(err => { console.error(err) });
        }
        else {
            console.log(upload_files[0].files.length,Folder.length,"piyan")
            alert("請上傳完整的檔案(資料夾)")
        }

    })

    const FrameChange = (data, index) => {
        modal_fill_frame[index].classList.remove("frame_none");
        upload_files[index].disabled = true;
        switch (index) {
            case 0:
                modal_fill_frame[index].innerHTML = `<i class="fa-solid fa-file"></i> <h3 class="fill_h3">${data[0].name}</h3>`;
                break;
            case 1:
                modal_fill_frame[index].innerHTML = `<i class="fa-solid fa-image"></i> <h3 class="fill_h3">${data[0].webkitRelativePath.split("/")[0]}</h3>`;
                break;
        }
    }

    const getData = (route) => {
        const file_route = "http://127.0.0.1:8000/return_file";
        fetch(file_route)
            .then(res => {
                if (!res.ok) {
                    alert("something wrong!")
                }
                else {
                    pdfFrame.src = file_route;
                }
            })
    }
    const StateAction = (state) => {
        switch (state) {
            case 0:
                break;
            case 1:
                alertText.style.opacity = 0;
                loader.style.opacity = 1;
                break;
            case 2:
                loader.style.opacity = 0;
                break;
        }
    }

})

