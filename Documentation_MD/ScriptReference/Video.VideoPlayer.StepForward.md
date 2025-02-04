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

#  [VideoPlayer](Video.VideoPlayer.html).StepForward

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

public void StepForward();

### Description

Immediately advance the current time by one frame.

If the video is currently playing, this method will pause the video before it
advances to the next frame. However, if the VideoPlayer isn't prepared, this
method will trigger preparation and display the first frame, but will not skip
to the next frame. It steps forward from non-initialized to frame 0.  
  
This method is useful if you want to:

  * Analyze each frame of a video.
  * Debug issues related to the video or elements that play at certain frames.
  * Take finer control over the playback speed, because you can choose exactly when the next frame will appear. However, the WebGL implementation is unable to provide frame-accurate control due to platform limitations.

    
    
    using UnityEngine;
    using UnityEngine.Video;
    using System.Collections;  
      
    // In the Inspector of your [GameObject](GameObject.html), attach this script and a [VideoPlayer](Video.VideoPlayer.html) component. 
    // Also, assign a [VideoClip](Video.VideoClip.html) to your [VideoPlayer](Video.VideoPlayer.html) component.  
    // Use this script to cycle through a video frame by frame.   
      
    public class StepForwardExample : [MonoBehaviour](MonoBehaviour.html)
    {
        [VideoPlayer](Video.VideoPlayer.html) videoPlayer;  
      
        public void Start()
        {
            videoPlayer = GetComponent<[VideoPlayer](Video.VideoPlayer.html)>();
            videoPlayer.Pause();
        }  
      
        private void [Update](PlayerLoop.Update.html)()
        {
            if ([Input.GetKeyDown](Input.GetKeyDown.html)("space") && videoPlayer.isPrepared)
            {
                [Debug.Log](Debug.Log.html)("[Space](Space.html) key pressed."); 
                // Go forward one frame in the video when you press the Spacebar. 
                videoPlayer.StepForward(); 
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

