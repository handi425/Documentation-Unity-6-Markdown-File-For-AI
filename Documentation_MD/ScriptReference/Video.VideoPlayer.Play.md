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

#  [VideoPlayer](Video.VideoPlayer.html).Play

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

public void Play();

### Description

Starts or resumes the playback of a video.

If the video isn't prepared, this method will prepare the video before it
starts playback, but playback won't be instant. To make playback instant, use
[VideoPlayer.Prepare](Video.VideoPlayer.Prepare.html) and wait for preparation
to finish (when [VideoPlayer.prepareCompleted](Video.VideoPlayer-
prepareCompleted.html) fires), before you use this method.  
  
If you use [VideoPlayer.Prepare](Video.VideoPlayer.Prepare.html) and then play
the video before preparation finishes, the VideoPlayer will finish preparation
and then play the video.  
  
Additional resources: [VideoPlayer.isPlaying](Video.VideoPlayer-
isPlaying.html), [VideoPlayer.Pause](Video.VideoPlayer.Pause.html),
[VideoPlayer.started](Video.VideoPlayer-started.html).

    
    
    using UnityEngine;
    using UnityEngine.Video;  
      
    public class PlayExample : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            // Get the [VideoPlayer](Video.VideoPlayer.html) attached to this [GameObject](GameObject.html).
            // You need to attach a [VideoPlayer](Video.VideoPlayer.html) component in the Inspector for this script to work. 
            var videoPlayer = GetComponent<[VideoPlayer](Video.VideoPlayer.html)>();  
      
            videoPlayer.Play();  
      
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

