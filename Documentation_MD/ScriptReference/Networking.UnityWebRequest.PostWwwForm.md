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

#  [UnityWebRequest](Networking.UnityWebRequest.html).PostWwwForm

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
PostWwwForm(string uri, string form);

## Declaration

public static [Networking.UnityWebRequest](Networking.UnityWebRequest.html)
PostWwwForm(Uri uri, string form);

### Parameters

uri | The target URI to which form data will be transmitted.  
---|---  
form | An HTML form to send.  
  
### Returns

**UnityWebRequest** A UnityWebRequest configured to send form data to `uri`
via `POST`.

### Description

Creates a UnityWebRequest configured to send form data to a server via HTTP
`POST`.

This method creates a UnityWebRequest, sets the `uri` and sets the method to
`POST`. The `Content-Type` header will be set to `application/x-www-form-
urlencoded` by default.  
  
This method attaches a
[DownloadHandlerBuffer](Networking.DownloadHandlerBuffer.html) to the
[UnityWebRequest](Networking.UnityWebRequest.html). This is for convenience,
as we anticipate most users will use the
[DownloadHandler](Networking.DownloadHandler.html) to check replies from the
server, particularly in the case of REST APIs.  
  
The string in the `form` parameter is expected to be a preformatted HTML form.
It will be escaped and sent as UTF-8 string.

    
    
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
            using ([UnityWebRequest](Networking.UnityWebRequest.html) www = [UnityWebRequest.PostWwwForm](Networking.UnityWebRequest.PostWwwForm.html)("https://www.my-server.com/myapi", "field1=1&field2=value2"))
            {
                yield return www.SendWebRequest();  
      
                if (www.result != [UnityWebRequest.Result.Success](Networking.UnityWebRequest.Result.Success.html))
                {
                    [Debug.LogError](Debug.LogError.html)(www.error);
                }
                else
                {
                    [Debug.Log](Debug.Log.html)("Form upload complete!");
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

