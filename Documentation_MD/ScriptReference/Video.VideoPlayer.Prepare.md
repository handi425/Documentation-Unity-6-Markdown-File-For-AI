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

#  [VideoPlayer](Video.VideoPlayer.html).Prepare

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

public void Prepare();

### Description

Prepares the playback engine so that it's ready for playback.

To prepare, the playback engine reserves the resources vital for playback, and
preloads some of the content to be played. If the preparation succeeds, this
method emits the [VideoPlayer.prepareCompleted](Video.VideoPlayer-
prepareCompleted.html) event and sets
[VideoPlayer.isPrepared](Video.VideoPlayer-isPrepared.html) to `true`. The
VideoPlayer is then ready to display the frames immediately and you can access
all properties related to the source.  
  
If you don't prepare the VideoPlayer before you play a video, the
[VideoPlayer.Play](Video.VideoPlayer.Play.html) method will do the preparation
but the video won't play instantly. If you use
[VideoPlayer.Stop](Video.VideoPlayer.Stop.html), the VideoPlayer becomes
unprepared again because it frees its resources for performance reasons. To
halt a video but keep its preparation, use
[VideoPlayer.Pause](Video.VideoPlayer.Pause.html) instead.  
  
Additional resources: [VideoPlayer.isPrepared](Video.VideoPlayer-
isPrepared.html).

    
    
    using UnityEngine;
    using UnityEngine.UI;
    using UnityEngine.Video;
     
    // The button to play the video in the script only becomes interactable after the preparation is finished.
    // To start the preparation process, press the [Space](Space.html) key in Play mode.   
      
    // Attach this script to the [GameObject](GameObject.html) you want to play a video clip on. 
    // Attach a [VideoPlayer](Video.VideoPlayer.html) component with a video clip and assign a UI [Button](UIElements.Button.html) in the Inspector.  
      
    public class PrepareExample: [MonoBehaviour](MonoBehaviour.html)
    {
        [VideoPlayer](Video.VideoPlayer.html) videoPlayer;
        public [Button](UIElements.Button.html) playButton;  
      
        private void Awake()
        {
            // Get the [VideoPlayer](Video.VideoPlayer.html) component attached to [GameObject](GameObject.html) with this script attached.  
            videoPlayer = GetComponent<[VideoPlayer](Video.VideoPlayer.html)>();
            // Attach the event handler, which triggers when the [VideoPlayer](Video.VideoPlayer.html) finishes its preparation. 
            videoPlayer.prepareCompleted += OnPrepareCompleted;
            videoPlayer.playOnAwake = false;
            playButton.interactable = false;
        }  
      
        // [Event](Event.html) handler for when [VideoPlayer](Video.VideoPlayer.html) finishes the preparation process. 
        void OnPrepareCompleted([VideoPlayer](Video.VideoPlayer.html) vp)
        {
            [Debug.Log](Debug.Log.html)("Preparation complete. You can now play the video.");
            
            // Preparation is complete so allow interactions with the play button. 
            playButton.interactable = true;
            playButton.onClick.AddListener(OnPlayButtonClicked);
        }  
      
        void OnPlayButtonClicked()
        {
            // If the play button is clicked and the preparation is done, play the video. 
            if(videoPlayer.isPrepared)
            {
                videoPlayer.Play();
            }
        }  
      
        private void [Update](PlayerLoop.Update.html)()
        {
            // Press Spacebar to prepare the video. 
            if ([Input.GetKeyDown](Input.GetKeyDown.html)("space"))
            {
                if (!videoPlayer.isPrepared)
                {
                    videoPlayer.Prepare(); 
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

