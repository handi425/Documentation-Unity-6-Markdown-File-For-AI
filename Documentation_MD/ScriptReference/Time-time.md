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

#  [Time](Time.html).time

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

public static float time;

### Description

The time at the beginning of the current frame in seconds since the start of
the application (Read Only).

This is the time in seconds since the start of the application, which
[Time.timeScale](Time-timeScale.html) scales and [Time.maximumDeltaTime](Time-
maximumDeltaTime.html) adjusts. When called from inside
[MonoBehaviour.FixedUpdate](MonoBehaviour.FixedUpdate.html), it returns
[Time.fixedTime](Time-fixedTime.html).  
  
This value is undefined during Awake messages and starts after all of these
messages are finished. This value does not update if the Editor is paused. See
[Time.realtimeSinceStartup](Time-realtimeSinceStartup.html) for a time value
that is unaffected by pausing.  
  
See [Time and Frame Rate Management](../Manual/managing-time-and-frame-
rate.html) in the User Manual for more information about how this property
relates to the other Time properties.

    
    
    //If the Fire1 button is pressed, a projectile
    //will be Instantiated every 0.5 seconds.  
      
    using UnityEngine;
    using System.Collections;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        public [GameObject](GameObject.html) projectile;
        public float fireRate = 0.5f;
        private float nextFire = 0.0f;  
      
        void [Update](PlayerLoop.Update.html)()
        {
            if ([Input.GetButton](Input.GetButton.html)("Fire1") && [Time.time](Time-time.html) > nextFire)
            {
                nextFire = [Time.time](Time-time.html) + fireRate;
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

