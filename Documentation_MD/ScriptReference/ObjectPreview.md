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

# ObjectPreview

class in UnityEditor

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

Base Class to derive from when creating Custom Previews.

You specify which type is the preview for by using the CustomPreview attribute
derived from [ObjectPreview](ObjectPreview.html). Below you can see an small
example that will display the name of the object being inspected. The preview
window will appear at the bottom of the Inspector window.

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    [CustomPreview(typeof([GameObject](GameObject.html)))]
    public class MyPreview : [ObjectPreview](ObjectPreview.html)
    {
        public override bool HasPreviewGUI()
        {
            return true;
        }  
      
        public override void OnPreviewGUI([Rect](Rect.html) r, [GUIStyle](GUIStyle.html) background)
        {
            [GUI.Label](GUI.Label.html)(r, target.name + " is being previewed");
        }
    }
    

### Properties

[target](ObjectPreview-target.html)| The object currently being previewed.  
---|---  
  
### Public Methods

[Cleanup](ObjectPreview.Cleanup.html)| Use this function to release resources
allocated by the ObjectPreview implementation.  
---|---  
[CreatePreview](ObjectPreview.CreatePreview.html)| See Editor.CreatePreview.  
[DrawPreview](ObjectPreview.DrawPreview.html)| This is the first entry point
for Preview Drawing.  
[GetInfoString](ObjectPreview.GetInfoString.html)| Implement this method to
show object information on top of the object preview.  
[GetPreviewTitle](ObjectPreview.GetPreviewTitle.html)| Override this method if
you want to change the label of the Preview area.  
[HasPreviewGUI](ObjectPreview.HasPreviewGUI.html)| Can this component be
Previewed in its current state?  
[Initialize](ObjectPreview.Initialize.html)| Called when the Preview gets
created with the objects being previewed.  
[MoveNextTarget](ObjectPreview.MoveNextTarget.html)| Called to iterate through
the targets, this will be used when previewing more than one target.  
[OnInteractivePreviewGUI](ObjectPreview.OnInteractivePreviewGUI.html)|
Implement to create your own interactive custom preview. Interactive custom
previews are used in the preview area of the inspector and the object
selector.  
[OnPreviewGUI](ObjectPreview.OnPreviewGUI.html)| Implement to create your own
custom preview for the preview area of the inspector, primary editor headers
and the object selector.  
[OnPreviewSettings](ObjectPreview.OnPreviewSettings.html)| Override this
method if you want to show custom controls in the preview header.  
[ResetTarget](ObjectPreview.ResetTarget.html)| Called to Reset the target
before iterating through them.  
  
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

