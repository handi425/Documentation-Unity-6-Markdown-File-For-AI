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

#
[UnityWebRequestMultimedia](Networking.UnityWebRequestMultimedia.html).GetAudioClip

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
GetAudioClip(string uri, [AudioType](AudioType.html) audioType);

## Declaration

public static [Networking.UnityWebRequest](Networking.UnityWebRequest.html)
GetAudioClip(Uri uri, [AudioType](AudioType.html) audioType);

### Parameters

uri | The URI of the audio clip to download.  
---|---  
audioType | The type of audio encoding for the downloaded audio clip. See [AudioType](AudioType.html).  
  
### Returns

**UnityWebRequest** A [UnityWebRequest](Networking.UnityWebRequest.html)
properly configured to download an audio clip and convert it to an
[AudioClip](AudioClip.html).

### Description

Create a [UnityWebRequest](Networking.UnityWebRequest.html) to download an
audio clip via HTTP GET and create an [AudioClip](AudioClip.html) based on the
retrieved data.

This method creates a [UnityWebRequest](Networking.UnityWebRequest.html) and
sets the target URL to the string `uri` argument. This method sets no other
flags or custom headers.  
  
This method attaches a
[DownloadHandlerAudioClip](Networking.DownloadHandlerAudioClip.html) object to
the [UnityWebRequest](Networking.UnityWebRequest.html).
[DownloadHandlerAudioClip](Networking.DownloadHandlerAudioClip.html) is a
specialized [DownloadHandler](Networking.DownloadHandler.html). It is
optimized for storing data which is to be used as an audio clip in the Unity
Engine. Using this class significantly reduces memory reallocation compared to
downloading raw bytes and creating an audio clip manually in script.  
  
This method attaches no [UploadHandler](Networking.UploadHandler.html) to the
[UnityWebRequest](Networking.UnityWebRequest.html).

    
    
    using UnityEngine;
    using UnityEngine.Networking;
    using System.Collections;  
      
    public class MyBehaviour : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            StartCoroutine(GetAudioClip());
        }  
      
        IEnumerator GetAudioClip()
        {
            using ([UnityWebRequest](Networking.UnityWebRequest.html) www = [UnityWebRequestMultimedia.GetAudioClip](Networking.UnityWebRequestMultimedia.GetAudioClip.html)("https://www.my-server.com/audio.ogg", [AudioType.OGGVORBIS](AudioType.OGGVORBIS.html)))
            {
                yield return www.SendWebRequest();  
      
                if (www.result == [UnityWebRequest.Result.ConnectionError](Networking.UnityWebRequest.Result.ConnectionError.html))
                {
                    [Debug.Log](Debug.Log.html)(www.error);
                }
                else
                {
                    [AudioClip](AudioClip.html) myClip = [DownloadHandlerAudioClip.GetContent](Networking.DownloadHandlerAudioClip.GetContent.html)(www);
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

