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

#  [UnityWebRequest](Networking.UnityWebRequest.html).Put

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

## Declaration

public static [Networking.UnityWebRequest](Networking.UnityWebRequest.html)
Put(string uri, byte[] bodyData);

## Declaration

public static [Networking.UnityWebRequest](Networking.UnityWebRequest.html)
Put(string uri, string bodyData);

## Declaration

public static [Networking.UnityWebRequest](Networking.UnityWebRequest.html)
Put(Uri uri, byte[] bodyData);

## Declaration

public static [Networking.UnityWebRequest](Networking.UnityWebRequest.html)
Put(Uri uri, string bodyData);

### Parameters

uri | The URI to which the data will be sent.  
---|---  
bodyData | The data to transmit to the remote server.  
  
If a string, the string will be converted to raw bytes via
[System.Text.Encoding.UTF8](https://msdn.microsoft.com/en-
us/library/system.text.encoding.utf8).  
  
### Returns

**UnityWebRequest** A UnityWebRequest configured to transmit `bodyData` to
`uri` via HTTP PUT.

### Description

Creates a UnityWebRequest configured to upload raw data to a remote server via
HTTP PUT.

This method creates a UnityWebRequest, sets the target URL to the string `uri`
argument and the `method` to `PUT`. It also sets the `Content-Type` header to
`application/octet-stream`.  
  
This method attaches a standard
[DownloadHandlerBuffer](Networking.DownloadHandlerBuffer.html) to the
UnityWebRequest. This is for convenience during development, as well as for
applications which return status information regarding the uploaded data in
the HTTP response body.  
  
This method stores the input upload data in an
[UploadHandlerRaw](Networking.UploadHandlerRaw.html) object and attaches it to
the [UnityWebRequest](Networking.UnityWebRequest.html).
[UploadHandlerRaw](Networking.UploadHandlerRaw.html) copies the input data
into a buffer. Therefore, changes to the `bodyData` array performed after the
call to this method will not be reflected in the data sent to the server.

    
    
    using UnityEngine;
    using UnityEngine.Networking;
    using System.Collections;  
      
    public class MyBehavior : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            StartCoroutine(Upload());
        }  
      
        IEnumerator Upload()
        {
            byte[] myData = System.Text.Encoding.UTF8.GetBytes("This is some test data");
            using ([UnityWebRequest](Networking.UnityWebRequest.html) www = [UnityWebRequest.Put](Networking.UnityWebRequest.Put.html)("https://www.my-server.com/upload", myData))
            {
                yield return www.SendWebRequest();  
      
                if (www.result != [UnityWebRequest.Result.Success](Networking.UnityWebRequest.Result.Success.html))
                {
                    [Debug.Log](Debug.Log.html)(www.error);
                }
                else
                {
                    [Debug.Log](Debug.Log.html)("Upload complete!");
                }
            }
        }
    }
    

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

