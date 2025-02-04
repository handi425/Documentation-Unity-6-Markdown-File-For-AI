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

#  [AudioMixer](Audio.AudioMixer.html).SetFloat

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

public bool SetFloat(string name, float value);

### Parameters

name | The name of an exposed Audio Mixer group parameter. To expose a parameter, go to the Audio Mixer group's Inspector window, right click the parameter you want to expose, and choose **Expose [parameter name] to script**.  
---|---  
value | Use to set the exposed Audio Mixer group parameter to a new value.  
  
### Returns

**bool** Returns false if the exposed parameter was not found or snapshots are
currently being edited.

### Description

Sets the value of the exposed parameter specified. When a parameter is
exposed, it is not controlled by mixer snapshots. You can only change the
parameter with this function.

**Note:** Don’t call AudioMixer.SetFloat in the following event functions as
it can result in unexpected behavior:

  * [MonoBehaviour.Awake](MonoBehaviour.Awake.html)
  * OnEnable
  * RuntimeInitializeLoadType.AfterSceneLoad

Instead, call [AudioMixer.SetFloat](Audio.AudioMixer.SetFloat.html) in
[MonoBehaviour.Start](MonoBehaviour.Start.html) or any event function Unity
calls afterwards in [Order of execution for event
functions](../Manual/execution-order.html).  
  
To see your exposed parameters,

  1. Double click on your audio mixer. This opens the **Audio Mixer** window.
  2. At the top right of the Audio Mixer tab, click on the **Exposed Parameters** button to show the list of exposed parameters. 

To rename or remove a parameter, right click the item in the list.  
  
If the parameter you want to expose isn't in the list, you need to expose the
parameter. To expose a parameter, right click the parameter you want to expose
in the Audio Mixer Inspector window, and choose **Expose [parameter name] to
script**.

    
    
    using [System](Rendering.VirtualTexturing.System.html);
    using UnityEngine;
    using UnityEngine.Audio;  
      
    public class MixerVolumeController : [MonoBehaviour](MonoBehaviour.html)
    {
        // The range of the volume slider on a mixer group
        const float minVolume = -80f;
        const float maxVolume = 20f;  
      
        public [AudioMixer](Audio.AudioMixer.html) mixer;  
      
        [Range(minVolume, maxVolume)]
        public float volume;  
      
        float previousVolume;  
      
        void [Update](PlayerLoop.Update.html)()
        {  
      
            // Sets the exposed parameter "volume" in the audio mixer,
            // In this example the parameter is assumed to be the volume of a mixer group.
            // It could be any other exposable mixer parameter.
            if (![Mathf.Approximately](Mathf.Approximately.html)(volume, previousVolume))
            {
                mixer.SetFloat("volume", volume);
            }  
      
            previousVolume = volume;
        }  
      
        void OnGUI()
        {
            [GUILayout.BeginHorizontal](GUILayout.BeginHorizontal.html)();
            [GUILayout.Label](GUILayout.Label.html)("Mixer volume");
            var newVolume = [GUILayout.HorizontalSlider](GUILayout.HorizontalSlider.html)(volume, minVolume, maxVolume, [GUILayout.Width](GUILayout.Width.html)(300));  
      
            if (![Mathf.Approximately](Mathf.Approximately.html)(newVolume, previousVolume))
            {
                volume = newVolume;
                mixer.SetFloat("volume", volume);
            }  
      
            [GUILayout.EndHorizontal](GUILayout.EndHorizontal.html)();
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

