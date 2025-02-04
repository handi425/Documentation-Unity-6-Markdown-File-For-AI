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

#  [NavMesh](AI.NavMesh.html).SetAreaCost

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

public static void SetAreaCost(int areaIndex, float cost);

### Parameters

areaIndex | Index of the area to set.  
---|---  
cost | New cost.  
  
### Description

Sets the cost for finding path over geometry of the area type on all agents.

This will replace any custom area costs on all agents, and set the default
cost for new agents that are created after calling the function. The cost must
be larger than 1.0.  
  
Use [GetAreaFromName](AI.NavMesh.GetAreaFromName.html) to find the area index
based on the name of the NavMesh area type.

    
    
    // ToggleWaterCost
    using UnityEngine;
    using UnityEngine.AI;  
      
    public class ToggleWaterCost : [MonoBehaviour](MonoBehaviour.html)
    {
        void [Update](PlayerLoop.Update.html)()
        {
            if ([Input.anyKeyDown](Input-anyKeyDown.html))
            {
                // Make the water area 10x more costly to traverse.
                [NavMesh.SetAreaCost](AI.NavMesh.SetAreaCost.html)([NavMesh.GetAreaFromName](AI.NavMesh.GetAreaFromName.html)("water"), 10.0f);
            }
        }
    }
    

Additional resources: [Areas and
Costs](https://docs.unity3d.com/Packages/com.unity.ai.navigation@2.0/manual/AreasAndCosts.html)
to learn how to use different Area types.

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

