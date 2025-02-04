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

#  [StaticEditorFlags](StaticEditorFlags.html).ContributeGI

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

Include the target [Mesh Renderer](../Manual/class-MeshRenderer.html) in
global illumination calculations.

These calculations take place while precomputing lighting data at bake time.
The ContributeGI property exposes the [ReceiveGI](ReceiveGI.html) property.
The ContributeGI property only takes effect if you enable a global
illumination setting such as [Baked Global Illumination](../Manual/class-
LightingSettings.html#MixedLighting.html) or [Enlighten Realtime Global
Illumination](../Manual/class-LightingSettings.html#RealtimeLighting.html) for
the target Scene. For additional context, see [this tutorial for setting up
the Built-in Render Pipeline and
lighting](../Manual/BestPracticeLightingPipelines.html) in Unity.

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);
    public class StaticEditorFlagsExample
    {
        [[MenuItem](MenuItem.html)("Examples/Create [GameObject](GameObject.html) and set Static [Editor](Editor.html) [Flags](Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetrics.Flags.html)")]
        static void CreateGameObjectAndSetStaticEditorFlags()
        {
            // Create a [GameObject](GameObject.html)
            var go = new [GameObject](GameObject.html)("Example");
            // Set the [GameObject](GameObject.html)'s [StaticEditorFlags](StaticEditorFlags.html)
            var flags = [StaticEditorFlags.ContributeGI](StaticEditorFlags.ContributeGI.html);
            [GameObjectUtility.SetStaticEditorFlags](GameObjectUtility.SetStaticEditorFlags.html)(go, flags);
        }
    }
    

Additional resources:
[GameObjectUtility.SetStaticEditorFlags](GameObjectUtility.SetStaticEditorFlags.html),
[GameObject.isStatic](GameObject-isStatic.html).

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

