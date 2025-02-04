[ ]()

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

LanguageEnglish

  * [English]()

  * C#

[ ](https://docs.unity3d.com)

## Scripting API

Version: Unity 6 Select a different version

LanguageEnglish

  * [English]()

# UploadHandlerFile

class in UnityEngine.Networking

/

Inherits from:[Networking.UploadHandler](Networking.UploadHandler.html)

/

Implemented
in:[UnityEngine.UnityWebRequestModule](UnityEngine.UnityWebRequestModule.html)

Leave feedback

Suggest a change

## Success!

Thank you for helping us improve the quality of Unity Documentation. Although
we cannot accept all submissions, we do read each suggested change from our
users and will make updates where applicable.

Close

## Submission failed

For some reason your suggested change could not be submitted. Please <a>try
again</a> in a few minutes. And thank you for taking the time to help us
improve the quality of Unity Documentation.

Close

Your name Your email Suggestion* Submit suggestion

Cancel

[ ]()

### Description

A specialized UploadHandler that reads data from a given file and sends raw
bytes to the server as the request body.

You can use it to send a large amount of data to the server with a low memory
footprint.

    
    
    using System.Collections;
    using UnityEngine;
    using UnityEngine.Networking;  
      
    public class UHFileSample : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            StartCoroutine(UploadFileData());
        }  
      
        IEnumerator UploadFileData()
        {
            using (var uwr = new [UnityWebRequest](Networking.UnityWebRequest.html)("https://yourwebsite.com/upload", [UnityWebRequest.kHttpVerbPUT](Networking.UnityWebRequest-kHttpVerbPUT.html)))
            {
                uwr.uploadHandler = new [UploadHandlerFile](Networking.UploadHandlerFile.html)("/path/to/file");
                yield return uwr.SendWebRequest();
                if (uwr.result != [UnityWebRequest.Result.Success](Networking.UnityWebRequest.Result.Success.html))
                    [Debug.LogError](Debug.LogError.html)(uwr.error);
                else
                {
                    // file data successfully sent
                }
            }
        }
    }
    

### Constructors

[UploadHandlerFile](Networking.UploadHandlerFile-ctor.html)| Create a new
upload handler to send data from the given file to the server.  
---|---  
  
### Inherited Members

### Properties

[contentType](Networking.UploadHandler-contentType.html)| Determines the
default Content-Type header which will be transmitted with the outbound HTTP
request.  
---|---  
[data](Networking.UploadHandler-data.html)| The raw data which will be
transmitted to the remote server as body data. (Read Only)  
[progress](Networking.UploadHandler-progress.html)| Returns the proportion of
data uploaded to the remote server compared to the total amount of data to
upload. (Read Only)  
  
### Public Methods

[Dispose](Networking.UploadHandler.Dispose.html)| Signals that this
UploadHandler is no longer being used, and should clean up any resources it is
using.  
---|---  
  
Is something described here not working as you expect it to? It might be a
**Known Issue**. Please check with the Issue Tracker at
[issuetracker.unity3d.com](https://issuetracker.unity3d.com).

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from:
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://unity3d.com/learn) [Community
Answers](https://answers.unity3d.com) [Knowledge
Base](https://support.unity3d.com/hc/en-us)
[Forums](https://forum.unity3d.com) [Asset Store](https://unity3d.com/asset-
store) [Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)
[Legal](https://unity.com/legal) [Privacy
Policy](https://unity.com/legal/privacy-policy)
[Cookies](https://unity.com/legal/cookie-policy) [Do Not Sell or Share My
Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

