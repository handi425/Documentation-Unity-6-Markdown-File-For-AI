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

#  [UnityWebRequest](Networking.UnityWebRequest.html).timeout

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

public int timeout;

### Description

Sets UnityWebRequest to attempt to abort after the number of seconds in
`timeout` have passed.

When a timeout occurs [error](Networking.UnityWebRequest-error.html) returns
"Request timeout" . No timeout is applied when `timeout` is set to `0` and
this property defaults to `0`.  
**Note:** The set timeout may apply to each URL redirect on Android which can
result in a longer response.

    
    
    using UnityEngine;
    using System.Collections;
    using UnityEngine.Networking;  
      
    // Ask the website to deliver an image that is very large.
    // Set the download to take more than 1 second.  This causes
    // the "request timeout" error message.  
      
    public class ExampleScript : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            StartCoroutine(GetText());
        }  
      
        IEnumerator GetText()
        {
            using [UnityWebRequest](Networking.UnityWebRequest.html) www = [UnityWebRequest.Get](Networking.UnityWebRequest.Get.html)("https://my-website.com/verylargeimage.jpg");  
      
            // wait up to one second to download the image
            www.timeout = 1;
            yield return www.SendWebRequest();  
      
            if (www.result != [UnityWebRequest.Result.Success](Networking.UnityWebRequest.Result.Success.html))
            {
                [Debug.LogError](Debug.LogError.html)(www.error);
            }
            else
            {
                [Debug.Log](Debug.Log.html)("image arrived");
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

