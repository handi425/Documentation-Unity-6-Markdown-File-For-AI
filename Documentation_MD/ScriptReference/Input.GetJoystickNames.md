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

#  [Input](Input.html).GetJoystickNames

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

public static string[] GetJoystickNames();

### Returns

**string[]** Returns an array of joystick and gamepad device names.

### Description

Retrieves a list of input device names corresponding to the index of an Axis
configured within Input Manager.

**Note: This API is part of the legacy** `Input` **class, and not recommended
for new projects. The documentation is provided here to support legacy
projects that use the old Input Manager and Input class. For new projects you
should use the newer and Input System Package**. ([read
more](../Manual/Input.html)).  
  
The strings returned are taken from the connected device's "friendly name" as
reported by the operating system. That is, the names are not fixed and will
likely vary between devices, drivers, and the OS itself.  
  
These strings are intended for use within input configuration screens \- this
way, instead of showing labels like "Joystick 1", you can show more meaningful
names like "Logitech WingMan". To read values from different joysticks, you
need to assign respective axes for the number of joysticks you want to support
in the Input Manager.  
  
The position of a joystick in this array corresponds to the joystick number,
i.e. the name in position 0 of this array is for the joystick that feeds data
into 'Joystick 1' in the Input Manager, the name in position 1 corresponds to
'Joystick 2', and so on. Note that some entries in the array may be blank if
no device is connected for that joystick number.

    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        // Prints a joystick name if movement is detected.  
      
        void [Update](PlayerLoop.Update.html)()
        {
            // requires you to set up axes "Joy0X" - "Joy3X" and "Joy0Y" - "Joy3Y" in the [Input](Input.html) Manager
            for (int i = 0; i < 4; i++)
            {
                if ([Mathf.Abs](Mathf.Abs.html)([Input.GetAxis](Input.GetAxis.html)("Joy" + i + "X")) > 0.2 ||
                    [Mathf.Abs](Mathf.Abs.html)([Input.GetAxis](Input.GetAxis.html)("Joy" + i + "Y")) > 0.2)
                {
                    [Debug.Log](Debug.Log.html)([Input.GetJoystickNames](Input.GetJoystickNames.html)()[i] + " is moved");
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

