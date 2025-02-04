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

#  [ToolAttribute](EditorTools.ToolAttribute.html).variantGroup

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

public Type variantGroup;

### Description

Tool variants are used to group logically similar tools into a single button
in the Tools Overlay.

The variantGroup type acts a key to specify groups of tools that should be
considered a group in the UI.

    
    
    using [System](Rendering.VirtualTexturing.System.html);
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.EditorTools;
    using UnityEngine;
    
    namespace GlobalToolVariants
    {
        // Define 3 tools that should be shown as a single button in the [Tools](Tools.html) [Overlay](Overlays.Overlay.html).
        struct ShapeVariantGroup {}
    
        [[EditorTool](EditorTools.EditorTool.html)("Line (Custom Global)", variantGroup = typeof(ShapeVariantGroup), variantPriority = 2)]
        [Icon("Assets/Examples/Icons/[Variant](UIElements.ToolbarMenu.Variant.html)-Line.png")]
        class Line : [EditorTool](EditorTools.EditorTool.html) {}
    
        [[EditorTool](EditorTools.EditorTool.html)("Circle (Custom Global)", variantGroup = typeof(ShapeVariantGroup), variantPriority = 1)]
        [Icon("Assets/Examples/Icons/[Variant](UIElements.ToolbarMenu.Variant.html)-Circle.png")]
        class Circle : [EditorTool](EditorTools.EditorTool.html) {}
    
        [[EditorTool](EditorTools.EditorTool.html)("Square (Custom Global)", variantGroup = typeof(ShapeVariantGroup), variantPriority = 0)]
        [Icon("Assets/Examples/Icons/[Variant](UIElements.ToolbarMenu.Variant.html)-Square.png")]
        class Square : [EditorTool](EditorTools.EditorTool.html) {}
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

