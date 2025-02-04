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

# SceneQueryEngineParameterTransformerAttribute

class in UnityEditor.Search.Providers

/

Inherits
from:[Search.QueryEngineParameterTransformerAttribute](Search.QueryEngineParameterTransformerAttribute.html)

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

Attribute class that defines a custom parameter transformer function applied
for a query running in a scene provider defined by a scene custom filter using
[SceneQueryEngineFilterAttribute](Search.Providers.SceneQueryEngineFilterAttribute.html).

    
    
    [SceneQueryEngineParameterTransformer]
    static [Vector3](Vector3.html) DistanceParamHandler(string param)
    {
        if (param == "selection")
        {
            var centerPoint = Selection.gameObjects.Select(go => go.transform.position).Aggregate((v1, v2) => v1 + v2);
            centerPoint /= Selection.gameObjects.Length;
            return centerPoint;
        }
    
        if (param.StartsWith("[") && param.EndsWith("]"))
        {
            param = param.Trim('[', ']');
            var vectorTokens = param.Split(',');
            var vectorValues = vectorTokens.Select(token => float.Parse(token, CultureInfo.InvariantCulture.NumberFormat)).ToList();
            while (vectorValues.Count < 3)
                vectorValues.Add(0f);
            return new [Vector3](Vector3.html)(vectorValues[0], vectorValues[1], vectorValues[2]);
        }
    
        var obj = [GameObject.Find](GameObject.Find.html)(param);
        if (!obj)
            return [Vector3.zero](Vector3-zero.html);
        return obj.transform.position;
    }
    

Used with

    
    
    [SceneQueryEngineFilter("dist", "DistanceParamHandler", new[] {"=", "!=", "<", ">", "<=", ">="})]
    static float DistanceHandler([GameObject](GameObject.html) go, [Vector3](Vector3.html) p)
    {
        return (go.transform.position - p).magnitude;
    }
    

### Inherited Members

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

