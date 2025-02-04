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

# AdvancedDropdown

class in UnityEditor.IMGUI.Controls

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

Inherit from this class to implement your own drop-down control.

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;
    using UnityEditor.IMGUI.Controls;  
      
    class WeekdaysDropdown : [AdvancedDropdown](IMGUI.Controls.AdvancedDropdown.html)
    {
        public WeekdaysDropdown([AdvancedDropdownState](IMGUI.Controls.AdvancedDropdownState.html) state) : base(state)
        {
        }  
      
        protected override [AdvancedDropdownItem](IMGUI.Controls.AdvancedDropdownItem.html) BuildRoot()
        {
            var root = new [AdvancedDropdownItem](IMGUI.Controls.AdvancedDropdownItem.html)("Weekdays");  
      
            var firstHalf = new [AdvancedDropdownItem](IMGUI.Controls.AdvancedDropdownItem.html)("First half");
            var secondHalf = new [AdvancedDropdownItem](IMGUI.Controls.AdvancedDropdownItem.html)("Second half");
            var weekend = new [AdvancedDropdownItem](IMGUI.Controls.AdvancedDropdownItem.html)("Weekend");  
      
            firstHalf.AddChild(new [AdvancedDropdownItem](IMGUI.Controls.AdvancedDropdownItem.html)("Monday"));
            firstHalf.AddChild(new [AdvancedDropdownItem](IMGUI.Controls.AdvancedDropdownItem.html)("Tuesday"));
            secondHalf.AddChild(new [AdvancedDropdownItem](IMGUI.Controls.AdvancedDropdownItem.html)("Wednesday"));
            secondHalf.AddChild(new [AdvancedDropdownItem](IMGUI.Controls.AdvancedDropdownItem.html)("Thursday"));
            weekend.AddChild(new [AdvancedDropdownItem](IMGUI.Controls.AdvancedDropdownItem.html)("Friday"));
            weekend.AddChild(new [AdvancedDropdownItem](IMGUI.Controls.AdvancedDropdownItem.html)("Saturday"));
            weekend.AddChild(new [AdvancedDropdownItem](IMGUI.Controls.AdvancedDropdownItem.html)("Sunday"));  
      
            root.AddChild(firstHalf);
            root.AddChild(secondHalf);
            root.AddChild(weekend);  
      
            return root;
        }
    }  
      
    public class AdvancedDropdownTestWindow : [EditorWindow](EditorWindow.html)
    {
        void OnGUI()
        {
            var rect = [GUILayoutUtility.GetRect](GUILayoutUtility.GetRect.html)(new [GUIContent](GUIContent.html)("Show"), [EditorStyles.toolbarButton](EditorStyles-toolbarButton.html));
            if ([GUI.Button](GUI.Button.html)(rect, new [GUIContent](GUIContent.html)("Show"), [EditorStyles.toolbarButton](EditorStyles-toolbarButton.html)))
            {
                var dropdown = new WeekdaysDropdown(new [AdvancedDropdownState](IMGUI.Controls.AdvancedDropdownState.html)());
                dropdown.Show(rect);
            }
        }
    }
    

### Properties

[minimumSize](IMGUI.Controls.AdvancedDropdown-minimumSize.html)| Minimum size
of the drop-down window. By default, the drop-down will try to match the width
of the given rect or the rendered content.  
---|---  
  
### Public Methods

[Show](IMGUI.Controls.AdvancedDropdown.Show.html)| Call this method to show
the drop-down at the given position.  
---|---  
  
### Protected Methods

[BuildRoot](IMGUI.Controls.AdvancedDropdown.BuildRoot.html)| Implement this
method to generate the content of the drop-down. This method is called when
the drop-down is being shown.  
---|---  
[ItemSelected](IMGUI.Controls.AdvancedDropdown.ItemSelected.html)| Override
this method to get notified when an item is selected.  
  
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

