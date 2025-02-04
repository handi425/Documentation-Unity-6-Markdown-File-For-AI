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

#  [DeviceType](DeviceType.html).Handheld

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

### Description

A handheld device like mobile phone or a tablet.

    
    
    //Attach this script to a [GameObject](GameObject.html)
    //This script checks what device type the [Application](Application.html) is running on and outputs this to the console  
      
    using UnityEngine;  
      
    public class DeviceTypeExample : [MonoBehaviour](MonoBehaviour.html)
    {
        //This is the Text for the [Label](UIElements.Label.html) at the top of the screen
        string m_DeviceType;  
      
        void [Update](PlayerLoop.Update.html)()
        {
    //Output the device type to the console window
            [Debug.Log](Debug.Log.html)("[Device](tvOS.Device.html) type : " + m_DeviceType);  
      
            //Check if the device running this is a console
            if ([SystemInfo.deviceType](SystemInfo-deviceType.html) == [DeviceType.Console](DeviceType.Console.html))
            {
                //Change the text of the label
                m_DeviceType = "Console";
            }  
      
            //Check if the device running this is a desktop
            if ([SystemInfo.deviceType](SystemInfo-deviceType.html) == [DeviceType.Desktop](DeviceType.Desktop.html))
            {
                m_DeviceType = "Desktop";
            }  
      
            //Check if the device running this is a handheld
            if ([SystemInfo.deviceType](SystemInfo-deviceType.html) == [DeviceType.Handheld](DeviceType.Handheld.html))
            {
                m_DeviceType = "[Handheld](Handheld.html)";
            }  
      
            //Check if the device running this is unknown
            if ([SystemInfo.deviceType](SystemInfo-deviceType.html) == [DeviceType.Unknown](DeviceType.Unknown.html))
            {
                m_DeviceType = "Unknown";
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

