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

#  [AudioHighPassFilter](AudioHighPassFilter.html).highpassResonanceQ

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

[Switch to Manual](../Manual/class-AudioHighPassFilter.html "Go to
AudioHighPassFilter Component in the Manual")

public float highpassResonanceQ;

### Description

Determines how much the filter's self-resonance isdampened.

Higher Highpass resonance Q indicates a lower rate of energy loss i.e. the
oscillations die out more slowly.  
  
Highpass resonance Q value goes from 1.0 to 10.0. Default = 1.0.

    
    
    using UnityEngine;  
      
    [[RequireComponent](RequireComponent.html)(typeof([AudioSource](AudioSource.html)))]
    [[RequireComponent](RequireComponent.html)(typeof([AudioHighPassFilter](AudioHighPassFilter.html)))]
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        // Moves the Highpass Resonance Quality Factor from 0 to 10 following a Sinus function
        // Attach this to an audio source with a HighPassFilter to listen it working.  
      
        void [Update](PlayerLoop.Update.html)()
        {
            GetComponent<[AudioHighPassFilter](AudioHighPassFilter.html)>().highpassResonanceQ = ([Mathf.Sin](Mathf.Sin.html)([Time.time](Time-time.html)) * 5 + 5);
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

