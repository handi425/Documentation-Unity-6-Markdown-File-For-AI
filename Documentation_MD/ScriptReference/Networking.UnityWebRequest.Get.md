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

#  [UnityWebRequest](Networking.UnityWebRequest.html).Get

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
Get(string uri);

## Declaration

public static [Networking.UnityWebRequest](Networking.UnityWebRequest.html)
Get(Uri uri);

### Parameters

uri | The URI of the resource to retrieve via HTTP GET.  
---|---  
  
### Returns

**UnityWebRequest** An object that retrieves data from the uri.

### Description

Create a UnityWebRequest for HTTP GET.

Use the method to create a [UnityWebRequest](Networking.UnityWebRequest.html).
Set the target URL to the `uri` with a `string` or `Uri` argument. No custom
flags or headers are set.

    
    
    using UnityEngine;
    using UnityEngine.Networking;
    using System.Collections;  
      
    // [UnityWebRequest.Get](Networking.UnityWebRequest.Get.html) example  
      
    // Access a website and use [UnityWebRequest.Get](Networking.UnityWebRequest.Get.html) to download a page.
    // Also try to download a non-existing page. [Display](Display.html) the error.  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            // A correct website page.
            StartCoroutine(GetRequest("https://www.example.com"));  
      
            // A non-existing page.
            StartCoroutine(GetRequest("https://error.html"));
        }  
      
        IEnumerator GetRequest(string uri)
        {
            using ([UnityWebRequest](Networking.UnityWebRequest.html) webRequest = [UnityWebRequest.Get](Networking.UnityWebRequest.Get.html)(uri))
            {
                // [Request](PackageManager.Requests.Request.html) and wait for the desired page.
                yield return webRequest.SendWebRequest();  
      
                string[] pages = uri.Split('/');
                int page = pages.Length - 1;  
      
                switch (webRequest.result)
                {
                    case [UnityWebRequest.Result.ConnectionError](Networking.UnityWebRequest.Result.ConnectionError.html):
                    case [UnityWebRequest.Result.DataProcessingError](Networking.UnityWebRequest.Result.DataProcessingError.html):
                        [Debug.LogError](Debug.LogError.html)(pages[page] + ": [Error](PackageManager.Error.html): " + webRequest.error);
                        break;
                    case [UnityWebRequest.Result.ProtocolError](Networking.UnityWebRequest.Result.ProtocolError.html):
                        [Debug.LogError](Debug.LogError.html)(pages[page] + ": HTTP [Error](PackageManager.Error.html): " + webRequest.error);
                        break;
                    case [UnityWebRequest.Result.Success](Networking.UnityWebRequest.Result.Success.html):
                        [Debug.Log](Debug.Log.html)(pages[page] + ":\nReceived: " + webRequest.downloadHandler.text);
                        break;
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

