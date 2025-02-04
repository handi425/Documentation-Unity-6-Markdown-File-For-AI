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

#  [Time](Time.html).timeAsDouble

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

public static double timeAsDouble;

### Description

The double precision time at the beginning of this frame (Read Only). This is
the time in seconds since the start of the game.

Time.timeAsDouble is the amount of time in seconds that the application has
been running for. It is read-only.  
  
Double precision version of [time](Time-time.html). This offers more precision
than a float or single value, particularly over extended periods of real-world
time. In almost all cases, you should use the [timeAsDouble](Time-
timeAsDouble.html) equivalent over [time](Time-time.html).  
  
The application receives the current [Time.timeAsDouble](Time-
timeAsDouble.html) at the beginning of each frame, with the value increasing
per frame. A [timeAsDouble](Time-timeAsDouble.html) call per frame receives
the same value. When called from `FixedUpdate` it returns the
[Time.fixedTimeAsDouble](Time-fixedTimeAsDouble.html) property.  
  
Regular (per frame) calls should be avoided: [Time.timeAsDouble](Time-
timeAsDouble.html) is intended to supply the length of time the application
has been running for, and not the time per frame.  
  
The value of [Time.timeAsDouble](Time-timeAsDouble.html) is undefined during
`Awake` messages and starts after all messages are finished.
[Time.timeAsDouble](Time-timeAsDouble.html) does not update if the Editor is
paused. See [Time.realtimeSinceStartupAsDouble](Time-
realtimeSinceStartupAsDouble.html) for a time value that is unaffected by
pausing.

    
    
    //If the Fire1 button is pressed, a projectile
    //will be Instantiated every 0.5 seconds.  
      
    using UnityEngine;
    using System.Collections;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        public [GameObject](GameObject.html) projectile;
        public float fireRate = 0.5f;
        private double nextFire = 0.0f;  
      
        void [Update](PlayerLoop.Update.html)()
        {
            if ([Input.GetButton](Input.GetButton.html)("Fire1") && [Time.timeAsDouble](Time-timeAsDouble.html) > nextFire)
            {
                nextFire = [Time.timeAsDouble](Time-timeAsDouble.html) + fireRate;
                Instantiate(projectile, transform.position, transform.rotation);
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

