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

#  [Input](Input.html).gyro

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

public static [Gyroscope](Gyroscope.html) gyro;

### Description

Returns default gyroscope.

**Note: This API is part of the legacy** `Input` **class, and not recommended
for new projects. The documentation is provided here to support legacy
projects that use the old Input Manager and Input class. For new projects you
should use the newer and Input System Package**. ([read
more](../Manual/Input.html)).  
  
Use this to return the gyroscope details of your device. Ensure first that
your device has a gyroscope. Use Input.gyro.enabled to check this.  
  
Knowing the gyroscope details of a device enables you the ability to include
features that need to know a device’s orientation. Common uses include
changing camera angles or GameObject’s positions when a user rotates and moves
their device.

    
    
    //Attach this script to a [GameObject](GameObject.html) in your [Scene](SceneManagement.Scene.html).
    using UnityEngine;
    using UnityEngine.UI;  
      
    public class InputGyroExample : [MonoBehaviour](MonoBehaviour.html)
    {
        [Gyroscope](Gyroscope.html) m_Gyro;  
      
        void Start()
        {
            //Set up and enable the gyroscope (check your device has one)
            m_Gyro = [Input.gyro](Input-gyro.html);
            m_Gyro.enabled = true;
        }  
      
    //This is a legacy function, check out the UI section for other ways to create your UI
        void OnGUI()
        {
            //Output the rotation rate, attitude and the enabled state of the gyroscope as a [Label](UIElements.Label.html)
            [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(500, 300, 200, 40), "Gyro rotation rate " + m_Gyro.rotationRate);
            [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(500, 350, 200, 40), "Gyro attitude" + m_Gyro.attitude);
            [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(500, 400, 200, 40), "Gyro enabled : " + m_Gyro.enabled);
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

