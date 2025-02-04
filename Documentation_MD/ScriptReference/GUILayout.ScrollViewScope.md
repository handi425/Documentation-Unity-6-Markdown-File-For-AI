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

# ScrollViewScope

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

Disposable helper class for managing
[BeginScrollView](GUILayout.BeginScrollView.html) /
[EndScrollView](GUILayout.EndScrollView.html).

Automatically laid out scrollviews will take whatever content you have inside
them and display normally. If it doesn't fit, scrollbars will appear. A call
to BeginScrollView must always be matched with a call to EndScrollView.  
  
![](../StaticFiles/ScriptRefImages/GUILayoutScrollView.png)  
_Scroll View in the Game View.._

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        // The variable to control where the scrollview 'looks' into its child elements.
        public [Vector2](Vector2.html) scrollPosition;  
      
        // The string to display inside the scrollview. 2 buttons below add & clear this string.
        public string longString = "This is a long-ish string";  
      
        void OnGUI()
        {
            // Begin a scroll view. All rects are calculated automatically -
            // it will use up any available screen space and make sure contents flow correctly.
            // This is kept small with the last two parameters to force scrollbars to appear.
            using (var scrollViewScope = new [ScrollViewScope](GUILayout.ScrollViewScope.html)(scrollPosition, [GUILayout.Width](GUILayout.Width.html)(100), [GUILayout.Height](GUILayout.Height.html)(100)))
            {
                scrollPosition = scrollViewScope.scrollPosition;  
      
                // We just add a single label to go inside the scroll view. Note how the
                // scrollbars will work correctly with wordwrap.
                [GUILayout.Label](GUILayout.Label.html)(longString);  
      
                // Add a button to clear the string. This is inside the scroll area, so it
                // will be scrolled as well. Note how the button becomes narrower to make room
                // for the vertical scrollbar
                if ([GUILayout.Button](GUILayout.Button.html)("Clear"))
                    longString = "";
            }  
      
            // Now we add a button outside the scrollview - this will be shown below
            // the scrolling area.
            if ([GUILayout.Button](GUILayout.Button.html)("Add More Text"))
                longString += "\nHere is another line";
        }
    }
    

### Properties

[handleScrollWheel](GUILayout.ScrollViewScope-handleScrollWheel.html)| Whether
this ScrollView should handle scroll wheel events. (default: true).  
---|---  
[scrollPosition](GUILayout.ScrollViewScope-scrollPosition.html)| The modified
scrollPosition. Feed this back into the variable you pass in, as shown in the
example.  
  
### Constructors

[GUILayout.ScrollViewScope](GUILayout.ScrollViewScope-ctor.html)| Create a new
ScrollViewScope and begin the corresponding ScrollView.  
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

