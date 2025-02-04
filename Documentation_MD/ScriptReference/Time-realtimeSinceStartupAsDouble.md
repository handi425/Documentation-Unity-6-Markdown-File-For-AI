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

#  [Time](Time.html).realtimeSinceStartupAsDouble

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

public static double realtimeSinceStartupAsDouble;

### Description

The real time in seconds since the game started (Read Only). Double precision
version of [realtimeSinceStartup](Time-realtimeSinceStartup.html).

This offers more precision than a float or single value, particularly over
extended periods of real-world time. In almost all cases, use the
[realtimeSinceStartupAsDouble](Time-realtimeSinceStartupAsDouble.html)
equivalent over [realtimeSinceStartup](Time-realtimeSinceStartup.html). In
almost all cases you can and should use [Time.timeAsDouble](Time-
timeAsDouble.html) instead.  
  
Using realtimeSinceStartupAsDouble is useful if you want to set
[Time.timeScale](Time-timeScale.html) to zero to pause your application, but
still want to be able to measure time somehow. In Editor scripts, you can also
use realtimeSinceStartupAsDouble to measure time while the Editor is paused.  
  
realtimeSinceStartupAsDouble returns time as reported by the system timer.
Depending on the platform and the hardware, it might report the same time even
in several consecutive frames. If you're dividing something by time
difference, take this into account (for example, time difference might become
zero).

    
    
    using UnityEngine;
    using System.Collections;  
      
    // An FPS counter.
    // It calculates frames/second over each updateInterval,
    // so the display does not keep changing wildly.
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        public float updateInterval = 0.5F;
        private double lastInterval;
        private int frames = 0;
        private float fps;
        void Start()
        {
            lastInterval = [Time.realtimeSinceStartupAsDouble](Time-realtimeSinceStartupAsDouble.html);
            frames = 0;
        }  
      
        void OnGUI()
        {
            [GUILayout.Label](GUILayout.Label.html)("" + fps.ToString("f2"));
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            ++frames;
            double timeNow = [Time.realtimeSinceStartupAsDouble](Time-realtimeSinceStartupAsDouble.html);
            if (timeNow > lastInterval + updateInterval)
            {
                fps = (float)(frames / (timeNow - lastInterval));
                frames = 0;
                lastInterval = timeNow;
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

