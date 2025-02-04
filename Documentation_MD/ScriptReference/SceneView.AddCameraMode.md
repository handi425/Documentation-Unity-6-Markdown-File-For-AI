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

#  [SceneView](SceneView.html).AddCameraMode

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

public static [SceneView.CameraMode](SceneView.CameraMode.html)
AddCameraMode(string name, string section);

### Parameters

name | The name for the new mode.  
---|---  
section | The section in which the new mode will be added. This can be an existing or new section.  
  
### Returns

**CameraMode** A CameraMode with the provided name and section.

### Description

Add a custom camera mode to the Scene view camera mode list.

When a user-defined mode is selected, the Scene view will render as though the
"shaded" mode is selected.

    
    
    using System.Collections.Generic;
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;  
      
    // Using a ScriptableSingleton lets us initialize and cleanup any managed resources with OnEnable and OnDisable.
    class CustomCameraMode : ScriptableSingleton<CustomCameraMode>
    {
        // Initialize an instance of this class when the editor loads.
        [InitializeOnLoadMethod]
        static void Init() => _ = instance;  
      
        const string k_Name = "Positions as Colors";
        const string k_Section = "Miscellaneous";
        [Shader](Shader.html) m_ReplacementShader;
        Dictionary<[SceneView](SceneView.html), bool> m_Active = new Dictionary<[SceneView](SceneView.html), bool>();  
      
        void OnEnable()
        {
            // Make sure to only call AddCameraMode once. This adds the camera mode to all existing and future SceneViews.
            [SceneView.AddCameraMode](SceneView.AddCameraMode.html)(k_Name, k_Section);  
      
            // Custom modes are implemented through replacement shaders. We set the replacement shader during repaint events
            // in the OnSceneGUI callback.
            [SceneView.duringSceneGui](SceneView-duringSceneGui.html) += OnSceneGUI;  
      
            // Create a shader in your project with code below this example.
            m_ReplacementShader = [Shader.Find](Shader.Find.html)("Unlit/PositionAsColor");
        }  
      
        // If any managed resources are created in OnEnable, they should be cleaned up in OnDisable.
        void OnDisable()
        {
            [SceneView.duringSceneGui](SceneView-duringSceneGui.html) -= OnSceneGUI;
        }  
      
        void OnSceneGUI([SceneView](SceneView.html) view)
        {
            if (Event.current.type != [EventType.Repaint](EventType.Repaint.html))
                return;  
      
            // When the active camera mode changes, we need to update the replacement shader. The replacement shader and
            // tag are serialized for each scene view, and do not need to be re-applied every frame or after domain reloads.
            // Alternatively, you can make use of the `[SceneView.onCameraModeChanged](SceneView-onCameraModeChanged.html)` event to update the replacement shader.
            if(!m_Active.TryGetValue(view, out var wasActive))
                m_Active[view] = wasActive = false;  
      
            var isActive = view.cameraMode.drawMode == [DrawCameraMode.UserDefined](DrawCameraMode.UserDefined.html)
                 && view.cameraMode.name == k_Name
                 && view.cameraMode.section== k_Section;  
      
            if (wasActive == isActive)
                return;  
      
            m_Active[view] = isActive;  
      
            if(isActive)
                view.SetSceneViewShaderReplace(m_ReplacementShader, string.Empty);
            else
                view.SetSceneViewShaderReplace(null, null);
        }
    }
    

The source code for the shader used in the sample above is an example.

    
    
              [Shader](Shader.html) "Unlit/PositionAsColor"
    {
        SubShader
        {
            Tags { "RenderType"="Opaque" }
            [LOD](LOD.html) 100  
      
            [Pass](ShaderData.Pass.html)
            {
                CGPROGRAM
                #pragma vertex vert
                #pragma fragment frag  
      
                #include "UnityCG.cginc"  
      
                struct appdata
                {
                    float4 vertex : POSITION;
                };  
      
                struct v2f
                {
                    float4 vertex : SV_POSITION;
                    float4 color  : COLOR;
                };  
      
                v2f vert (appdata v)
                {
                    v2f o;
                    o.vertex = UnityObjectToClipPos(v.vertex);
                    o.color = float4((normalize(v.vertex.xyz)+1)*.5, 1);
                    return o;
                }  
      
                fixed4 frag (v2f i) : SV_Target
                {
                    return i.color;
                }
                ENDCG
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

