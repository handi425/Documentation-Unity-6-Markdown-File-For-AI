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

**Method group is Obsolete**  

#  [AudioClip](AudioClip.html).isReadyToPlay

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

[Switch to Manual](../Manual/class-AudioClip.html "Go to AudioClip Component
in the Manual")

**Obsolete** Use AudioClip.loadState instead to get more detailed information
about the loading process. public bool isReadyToPlay;

### Description

Returns true if the AudioClip is ready to play (read-only).

This applies to any type of AudioClip, regardless whether they load all data
at startup, dynamically in the background or streamed from disk or web. In the
first case the property will be true when the whole clip has been loaded,
while in the streamed cases it will be true when enough data is buffered to
start playback.

    
    
    using UnityEngine;
    using UnityEngine.Networking;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        [AudioSource](AudioSource.html) source;  
      
        void Start()
        {
            [UnityWebRequest](Networking.UnityWebRequest.html) webRequest = [UnityWebRequestMultimedia.GetAudioClip](Networking.UnityWebRequestMultimedia.GetAudioClip.html)("www.example.com", [AudioType.UNKNOWN](AudioType.UNKNOWN.html));
            source = GetComponent<[AudioSource](AudioSource.html)>();
            source.clip = [DownloadHandlerAudioClip.GetContent](Networking.DownloadHandlerAudioClip.GetContent.html)(webRequest);
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            if (!source.isPlaying && source.clip.isReadyToPlay)
            {
                source.Play();
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

