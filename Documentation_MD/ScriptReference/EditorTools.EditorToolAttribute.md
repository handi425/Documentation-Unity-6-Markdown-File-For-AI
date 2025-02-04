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

# EditorToolAttribute

class in UnityEditor.EditorTools

/

Inherits from:[EditorTools.ToolAttribute](EditorTools.ToolAttribute.html)

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

Registers an [EditorTool](EditorTools.EditorTool.html) as either a Global tool
or a [Component](Component.html) tool for a specific target type.

A Global tool works on any selection. A Global tool is also always available
from the top toolbar. A Component tool, like a
[CustomEditor](CustomEditor.html), is only available for selections that match
a target type.

    
    
    using [System](Rendering.VirtualTexturing.System.html);
    using System.Collections.Generic;
    using System.Linq;
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.EditorTools;
    using UnityEngine.Rendering;
    
    // By passing `typeof([MeshFilter](MeshFilter.html))` as the second argument, we register VertexTool as a [CustomEditor](CustomEditor.html) tool to be presented
    // when the current selection contains a [MeshFilter](MeshFilter.html) component.
    [[EditorTool](EditorTools.EditorTool.html)("Show Vertices", typeof([MeshFilter](MeshFilter.html)))]
    class VertexTool : [EditorTool](EditorTools.EditorTool.html), [IDrawSelectedHandles](EditorTools.IDrawSelectedHandles.html)
    {
        struct TransformAndPositions
        {
            public [Transform](Transform.html) transform;
            public [Vector3](Vector3.html)[] positions;
        }
    
        IEnumerable<TransformAndPositions> m_Vertices;
        [GUIContent](GUIContent.html) m_ToolbarIcon;
    
        public override [GUIContent](GUIContent.html) toolbarIcon
        {
            get
            {
                if (m_ToolbarIcon == null)
                    m_ToolbarIcon = new [GUIContent](GUIContent.html)(
                        [AssetDatabase.LoadAssetAtPath](AssetDatabase.LoadAssetAtPath.html)<[Texture2D](Texture2D.html)>("Assets/Examples/Icons/VertexTool.png"),
                        "[Vertex](UIElements.Vertex.html) Visualization [Tool](Tool.html)");
                return m_ToolbarIcon;
            }
        }
    
        void OnEnable()
        {
            m_Vertices = targets.Select(x =>
            {
                return new TransformAndPositions()
                {
                    transform = (([MeshFilter](MeshFilter.html))x).transform,
                    positions = (([MeshFilter](MeshFilter.html))x).sharedMesh.vertices
                };
            }).ToArray();
        }
    
        public override void OnToolGUI([EditorWindow](EditorWindow.html) window)
        {
            foreach (var entry in m_Vertices)
            {
                var matrix = entry.transform.localToWorldMatrix;
                Drawing.DrawHandleCaps(matrix, entry.positions, [Color.cyan](Color-cyan.html) * .3f, .05f, [CompareFunction.Greater](Rendering.CompareFunction.Greater.html));
                Drawing.DrawHandleCaps(matrix, entry.positions, [Color.cyan](Color-cyan.html), .05f, [CompareFunction.LessEqual](Rendering.CompareFunction.LessEqual.html));
            }
        }
    
        public void OnDrawHandles()
        {
            if(![ToolManager.IsActiveTool](EditorTools.ToolManager.IsActiveTool.html)(this))
                return;
    
            foreach (var entry in m_Vertices)
            {
                var matrix = entry.transform.localToWorldMatrix;
                Drawing.DrawHandleCaps(matrix, entry.positions, [Color.cyan](Color-cyan.html) * .3f, .03f, [CompareFunction.Greater](Rendering.CompareFunction.Greater.html));
                Drawing.DrawHandleCaps(matrix, entry.positions, [Color.cyan](Color-cyan.html), .03f, [CompareFunction.LessEqual](Rendering.CompareFunction.LessEqual.html));
            }
        }
    }
    

You can also use tool variants to group similar tools into a single button in
the Tools overlay. Refer to
[ToolAttribute.variantGroup](EditorTools.ToolAttribute-variantGroup.html).

    
    
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
    

### Constructors

[EditorToolAttribute](EditorTools.EditorToolAttribute-ctor.html)| Registers an
EditorTool as either a Global tool or a CustomEditor tool.  
---|---  
  
### Inherited Members

### Static Properties

[defaultPriority](EditorTools.ToolAttribute-defaultPriority.html)| The default
value for ToolAttribute.toolPriority and ToolAttribute.variantPriority.
Specify a priority lower than this value to display a tool before the default
entries, or specify a higher value to display it after the default entries.  
---|---  
  
### Properties

[displayName](EditorTools.ToolAttribute-displayName.html)| The name that
displays in menus.  
---|---  
[targetContext](EditorTools.ToolAttribute-targetContext.html)| If provided,
the EditorTool will only be made available when the
ToolManager.activeContextType is equal to targetContext.  
[targetType](EditorTools.ToolAttribute-targetType.html)| Set to the type that
this EditorTool or EditorToolContext can edit. Set to null if the tool is not
specific to a Component and should be available at any time.  
[toolPriority](EditorTools.ToolAttribute-toolPriority.html)| Tool priority
defines the order that tools are displayed in within the Tools Overlay.  
[variantGroup](EditorTools.ToolAttribute-variantGroup.html)| Tool variants are
used to group logically similar tools into a single button in the Tools
Overlay.  
[variantPriority](EditorTools.ToolAttribute-variantPriority.html)| The variant
priority defines the order that tools are displayed in when they are displayed
in a ToolAttribute.variantGroup dropdown.  
  
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

