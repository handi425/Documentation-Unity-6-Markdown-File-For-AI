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

#  [GUI](GUI.html).enabled

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

public static bool enabled;

### Description

Is the GUI enabled?

Set this value to false to disable all GUI interaction. All controls will be
draw semi-transparently, and will not respond to user input.  
  
![](../StaticFiles/ScriptRefImages/GUIEnabled.png)  
_Enabled / Disabled GUI controls._

    
    
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        // The value tracking whether or not the extended options can be toggled.
        public bool allOptions = true;  
      
        // The 2 extended options.
        public bool extended1 = true;
        public bool extended2 = true;  
      
        void OnGUI()
        {
            // Make a toggle control that allows the user to edit some extended options.
            allOptions = [GUI.Toggle](GUI.Toggle.html)(new [Rect](Rect.html)(0, 0, 150, 20), allOptions, "Edit All [Options](Progress.Options.html)");  
      
            // Assign the value of it to the [GUI.enabled](GUI-enabled.html) - if the checkbox above
            // is disabled, so will these [GUI](GUI.html) elements be
            [GUI.enabled](GUI-enabled.html) = allOptions;  
      
            // These two controls will only be enabled if the button above is on.
            extended1 = [GUI.Toggle](GUI.Toggle.html)(new [Rect](Rect.html)(20, 20, 130, 20), extended1, "Extended Option 1");
            extended2 = [GUI.Toggle](GUI.Toggle.html)(new [Rect](Rect.html)(20, 40, 130, 20), extended2, "Extended Option 2");  
      
            // We're done with the conditional block, so make [GUI](GUI.html) code be enabled again.
            [GUI.enabled](GUI-enabled.html) = true;  
      
            // Make an Ok button
            if ([GUI.Button](GUI.Button.html)(new [Rect](Rect.html)(0, 60, 150, 20), "OK"))
            {
                print("user clicked ok");
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

