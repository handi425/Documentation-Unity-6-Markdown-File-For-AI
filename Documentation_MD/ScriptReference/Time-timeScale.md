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

#  [Time](Time.html).timeScale

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

public static float timeScale;

### Description

The scale at which time passes.

This can be used for slow motion effects or to speed up your application. When
timeScale is 1.0, time passes as fast as real time. When timeScale is 0.5 time
passes 2x slower than realtime.  
  
When timeScale is set to zero your application acts as if paused if all your
functions are frame rate independent. Negative values are ignored.  
  
Note that changing the timeScale only takes effect on the following frames.
How often [MonoBehaviour.FixedUpdate](MonoBehaviour.FixedUpdate.html) is
executed per frame depends on the timeScale. Therefore, to keep the number of
FixedUpdate callbacks per frame constant, you must also multiply
[Time.fixedDeltaTime](Time-fixedDeltaTime.html) by timeScale. Whether this
adjustment is desirable is game-specific.  
  
FixedUpdate functions and suspended Coroutines with
[WaitForSeconds](WaitForSeconds.html) are not called when timeScale is set to
zero.

    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        // Toggles the time scale between 1 and 0.7
        // whenever the user hits the Fire1 button.  
      
        private float fixedDeltaTime;  
      
        void Awake()
        {
            // Make a copy of the fixedDeltaTime, it defaults to 0.02f, but it can be changed in the editor
            this.fixedDeltaTime = [Time.fixedDeltaTime](Time-fixedDeltaTime.html);
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            if ([Input.GetButtonDown](Input.GetButtonDown.html)("Fire1"))
            {
                if ([Time.timeScale](Time-timeScale.html) == 1.0f)
                    [Time.timeScale](Time-timeScale.html) = 0.7f;
                else
                    [Time.timeScale](Time-timeScale.html) = 1.0f;
                // Adjust fixed delta time according to timescale
                // The fixed delta time will now be 0.02 real-time seconds per frame
                [Time.fixedDeltaTime](Time-fixedDeltaTime.html) = this.fixedDeltaTime * [Time.timeScale](Time-timeScale.html);
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

