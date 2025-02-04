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

#  [Light](Light.html).spotAngle

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

[Switch to Manual](../Manual/class-Light.html "Go to Light Component in the
Manual")

public float spotAngle;

### Description

The angle of the spot light's cone in degrees.

This is used primarily for [Spot](LightType.Spot.html) lights and has no
effect for [Point](LightType.Point.html) lights Additional resources: [Light
component](../Manual/class-Light.html).

    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        // Change spot angle randomly between 'minAngle' and 'maxAngle'
        // each 'interval' seconds.  
      
        float interval = 0.3f;
        float minAngle = 10;
        float maxAngle = 90;
        float timeLeft;  
      
        [Light](Light.html) lt;  
      
    
        void Start()
        {
            lt = GetComponent<[Light](Light.html)>();
            lt.type = [LightType.Spot](LightType.Spot.html);  
      
            timeLeft = interval;
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            timeLeft -= [Time.deltaTime](Time-deltaTime.html);  
      
            if (timeLeft < 0.0)
            {
                // time to change!
                timeLeft = interval;
                lt.spotAngle = [Random.Range](Random.Range.html)(minAngle, maxAngle);
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

