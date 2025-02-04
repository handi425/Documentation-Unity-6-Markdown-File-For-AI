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

#  [ScrollView](UIElements.ScrollView.html).ScrollTo

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

public void ScrollTo([UIElements.VisualElement](UIElements.VisualElement.html)
child);

### Parameters

child | The child to scroll to.  
---|---  
  
### Description

Scroll to a specific child element.

This example creates a ScrollView that contains multiple labels. A Button is
used to scroll to a selected label.

    
    
    using UnityEngine;
    using UnityEngine.UIElements;  
      
    public class ScrollViewScrollToExample : [MonoBehaviour](MonoBehaviour.html)
    {
        public [UIDocument](UIElements.UIDocument.html) uiDocument;
        public int numberOfLabels = 100;
        public int scrollToButton = 50;  
      
        [Label](UIElements.Label.html)[] labels;  
      
        void Start()
        {
            var sv = new [ScrollView](UIElements.ScrollView.html) { name = "My Scroll View" };  
      
            labels = new [Label](UIElements.Label.html)[numberOfLabels];
            for (int i = 0; i < numberOfLabels; i++)
            {
                var label = new [Label](UIElements.Label.html) { text = "[Button](UIElements.Button.html) " + i };
                labels[i] = label;
                sv.Add(label);
            }  
      
            var button = new [Button](UIElements.Button.html) { text = "Scroll to " + scrollToButton };
            button.clicked += DoScrollTo;  
      
            uiDocument.rootVisualElement.Add(button);
            uiDocument.rootVisualElement.Add(sv);
        }  
      
        void DoScrollTo()
        {
            var sv = uiDocument.rootVisualElement.Q<[ScrollView](UIElements.ScrollView.html)>("My Scroll View");
            sv.ScrollTo(labels[scrollToButton]);
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

