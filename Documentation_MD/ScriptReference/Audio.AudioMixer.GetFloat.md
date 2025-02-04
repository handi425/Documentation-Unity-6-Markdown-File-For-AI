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

#  [AudioMixer](Audio.AudioMixer.html).GetFloat

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

public bool GetFloat(string name, out float value);

### Parameters

name | Name of exposed parameter.  
---|---  
value | Return value of exposed parameter.  
  
### Returns

**bool** Returns false if the exposed parameter specified doesn't exist.

### Description

Returns the value of the exposed parameter specified. If the parameter doesn't
exist the function returns false. Prior to calling SetFloat and after
ClearFloat has been called on this parameter the value returned will be that
of the current snapshot or snapshot transition.

To see your exposed parameters,

  1. Double click on your audio mixer. This opens the Audio Mixer window.
  2. At the top right of the **Audio Mixer** window, click on the **Exposed Parameters** button to show the list of exposed parameters. 

To rename or remove a parameter, right click the item in the list.  
  
If the parameter you want to expose isn't in the list, you need to expose the
parameter. To expose a parameter, right click the parameter you want to expose
in the Audio Mixer Inspector window, and choose **Expose [parameter name] to
script**.

    
    
    using [System](Rendering.VirtualTexturing.System.html);
    using UnityEngine;
    using UnityEngine.Audio;  
      
    // 1. Attach this script to a [GameObject](GameObject.html) in your [Scene](SceneManagement.Scene.html).
    // 2. Create an Audio Mixer and expose some variables on it.
    // 3. Add an Audio Source to your [Scene](SceneManagement.Scene.html) and assign your Audio Mixer to it.   
      
    public class MixerVolumeController : [MonoBehaviour](MonoBehaviour.html)
    {
        // Make sure to assign your Audio Mixer in the Inspector window of the [GameObject](GameObject.html) you attach this script to.
        public [AudioMixer](Audio.AudioMixer.html) mixer;
        float volume, exposedParam;  
      
        void Start()
    {  
      
        // Gets the exposed parameters "MyExposedParam" and "volume" in the Audio Mixer.
        // "MyExposedParam" is the default name for exposed parameters.
     
        // "Volume is an exposed parameter that has been renamed. 
        // Change these names to what your exposed parameters are called.   
      
        mixer.GetFloat("MyExposedParam", out exposedParam);
        [Debug.Log](Debug.Log.html)("My Exposed Param: " + exposedParam);  
      
        mixer.GetFloat("Volume", out volume);
        [Debug.Log](Debug.Log.html)("Volume: " + volume);
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

