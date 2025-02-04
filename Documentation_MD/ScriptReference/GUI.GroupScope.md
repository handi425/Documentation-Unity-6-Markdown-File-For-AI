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

# GroupScope

class in UnityEngine

/

Implemented in:[UnityEngine.IMGUIModule](UnityEngine.IMGUIModule.html)

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

Disposable helper class for managing [BeginGroup](GUI.BeginGroup.html) /
[EndGroup](GUI.EndGroup.html).

[BeginGroup](GUI.BeginGroup.html) is called at construction, and
[EndGroup](GUI.EndGroup.html) is called when the instance is disposed. When
you begin a group, the coordinate system for GUI controls are set so (0,0) is
the top-left corner of the group. All controls are clipped to the group.
Groups can be nested - if they are, children are clipped to their parents.  
  
This is very useful when moving a bunch of GUI elements around on screen. A
common use case is designing your menus to fit on a specific screen size, then
centering the GUI on larger displays.

    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        void OnGUI()
        {
            // Constrain all drawing to be within a 800x600 pixel area centered on the screen.
            using (var groupScope = new [GUI.GroupScope](GUI.GroupScope.html)(new [Rect](Rect.html)([Screen.width](Screen-width.html) / 2 - 400, [Screen.height](Screen-height.html) / 2 - 300, 800, 600)))
            {
                // Draw a box in the new coordinate space defined by the BeginGroup.
                // Notice how (0,0) has now been moved on-screen.
                [GUI.Box](GUI.Box.html)(new [Rect](Rect.html)(0, 0, 800, 600), "This box is now centered! - here you would put your main menu");
            }
            // The group is now ended.
        }
    }
    

### Constructors

[GUI.GroupScope](GUI.GroupScope-ctor.html)| Create a new GroupScope and begin
the corresponding group.  
---|---  
  
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

