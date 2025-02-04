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

#  [EditorGUI](EditorGUI.html).hyperLinkClicked

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

### Parameters

value | The first parameter of type [EditorWindow](EditorWindow.html) corresponds to the window that contains the text that was clicked. The second parameter of type [HyperLinkClickedEventArgs](HyperLinkClickedEventArgs.html) contains the hyperlink data.  
---|---  
  
### Description

Event used to react on clicks on a text hyperlink part.

On a rich text string, a hyperlink is defined with the <a> tag.

    
    
    <a href="https://docs.unity3d.com">Documentation link</a>

The hyperlink parameters are returned in the
[HyperLinkClickedEventArgs](HyperLinkClickedEventArgs.html).  
  
In the example above, the
[HyperLinkClickedEventArgs.hyperLinkData](HyperLinkClickedEventArgs-
hyperLinkData.html) dictionary will have one element of key "href" and of
value "https://docs.unity3d.com".  
  
Do note that this parameter is already covered by default to open uri. It also
handles paths and you can add the line parameter to open the file directly on
a specific line.  
  
It is possible to have only part of a string in a hyperlink or even multiple
hyperlinks per string.

    
    
    This is the <a href=\"https://unity.com/\">unity website</a> and this is the <a href=\"https://docs.unity3d.com\">unity documentation website</a>

The event contains information only on the hyperlink part that is clicked.  
  
Use the window parameter in order to react only on hyperlinks that were
clicked in that window. If you don't filter on the window, you might react to
other hyperlinks like the ones in the Console or the Profiler.

    
    
    using [System](Rendering.VirtualTexturing.System.html);
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;
    
    class EditorGUIHyperLinkClicked : [EditorWindow](EditorWindow.html)
    {
        [[MenuItem](MenuItem.html)("Examples/EditorGUIHyperLinkClicked")]
        static void Init()
        {
            var window = GetWindow<EditorGUIHyperLinkClicked>();
            window.Show();
        }
    
        void OnGUI()
        {
            [GUIStyle](GUIStyle.html) style = new [GUIStyle](GUIStyle.html)() { richText = true };
            [EditorGUILayout.TextField](EditorGUILayout.TextField.html)("<a data=\"some data\" otherData=\"some other data\">displayed string</a>", style);
        }
    
        static EditorGUIHyperLinkClicked()
        {
            [EditorGUI.hyperLinkClicked](EditorGUI-hyperLinkClicked.html) += EditorGUI_hyperLinkClicked;
        }
    
        private static void EditorGUI_hyperLinkClicked([EditorWindow](EditorWindow.html) window, [HyperLinkClickedEventArgs](HyperLinkClickedEventArgs.html) args)
        {
            if (window.titleContent.text == "EditorGUIHyperLinkClicked")
            {
                var hyperLinkData = args.hyperLinkData;
                var data = hyperLinkData["data"];
                var otherData = hyperLinkData["otherData"];
    
                [Debug.Log](Debug.Log.html)($"data: {data}, otherData: {otherData}");
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

