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

# SearchActionsProviderAttribute

class in UnityEditor.Search

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

Attribute used to declare a static method that defines new actions for
specific search providers.

    
    
    using System.Collections.Generic;
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.Search;
    using UnityEngine;
    using UnityEngine.Rendering;
    
    public class Example_SearchAction
    {
        [SearchActionsProvider]
        internal static IEnumerable<[SearchAction](Search.SearchAction.html)> ActionHandlers()
        {
            return new[]
            {
                new [SearchAction](Search.SearchAction.html)("asset", "print_dependencies", new [GUIContent](GUIContent.html)("Print [Dependencies](Unity.Android.Gradle.Dependencies.html)", null, "Print all dependencies of an asset."))
                {
                    // If this action is the default, double-clicking on an item to execute this action will not close the Search window.
                    closeWindowAfterExecution = false,
    
                    // Handler for a single item.
                    handler = (item) =>
                    {
                        var asset = item.ToObject();
                        if (!asset)
                            return;
                        var path = [AssetDatabase.GetAssetPath](AssetDatabase.GetAssetPath.html)(asset);
                        if (string.IsNullOrEmpty(path))
                            return;
    
                        var dependencyPaths = [AssetDatabase.GetDependencies](AssetDatabase.GetDependencies.html)(path);
                        foreach (var dependencyPath in dependencyPaths)
                        {
                            var o = [AssetDatabase.LoadAssetAtPath](AssetDatabase.LoadAssetAtPath.html)<UnityEngine.Object>(dependencyPath);
                            if (o != null)
                                [Debug.Log](Debug.Log.html)(dependencyPath, o);
                        }
                    }
                },
    
                new [SearchAction](Search.SearchAction.html)("scene", "toggle_cast_shadows", new [GUIContent](GUIContent.html)("[Toggle](UIElements.Toggle.html) Cast Shadows", null, "[Toggle](UIElements.Toggle.html) Cast Shadows on a [Mesh](Mesh.html)"))
                {
                    // Only enable this action if any of the selected items are actually a [GameObject](GameObject.html) with a [MeshRenderer](MeshRenderer.html).
                    enabled = items =>
                    {
                        foreach (var searchItem in items)
                        {
                            var go = searchItem.ToObject<[GameObject](GameObject.html)>();
                            if (!go)
                                continue;
                            var mesh = go.GetComponent<[MeshRenderer](MeshRenderer.html)>();
                            if (mesh)
                                return true;
                        }
                        return false;
                    },
                    // Handler for multiple items: (used when multi selection is used in the Search Window).
                    execute = (items) =>
                    {
                        foreach (var searchItem in items)
                        {
                            var go = searchItem.ToObject<[GameObject](GameObject.html)>();
                            if (!go)
                                continue;
                            var mesh = go.GetComponent<[MeshRenderer](MeshRenderer.html)>();
                            if (!mesh)
                                continue;
                            mesh.shadowCastingMode = mesh.shadowCastingMode == [ShadowCastingMode.Off](Rendering.ShadowCastingMode.Off.html) ? [ShadowCastingMode.On](Rendering.ShadowCastingMode.On.html) : [ShadowCastingMode.Off](Rendering.ShadowCastingMode.Off.html);
                        }
                    }
                },
            };
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

