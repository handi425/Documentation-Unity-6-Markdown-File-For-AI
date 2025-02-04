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

#  [CollectionPool<T0,T1>](Pool.CollectionPool_2.html).Get

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

public static TCollection Get();

### Returns

**TCollection** A pooled object or a new instance if the pool is empty.

### Description

Get an instance from the pool. If the pool is empty then a new instance will
be created.

    
    
    using System.Collections.Generic;
    using UnityEngine;
    using UnityEngine.Pool;  
      
    // This example shows how both version of Get could be used to simplify a line of points.
    public class Simplify2DLine
    {
        public List<[Vector2](Vector2.html)> SimplifyLine([Vector2](Vector2.html)[] points)
        {
            // This version will only be returned to the pool if we call Release on it.
            var simplifiedPoints = CollectionPool<List<[Vector2](Vector2.html)>, [Vector2](Vector2.html)>.Get();  
      
            // Copy the points into a temp list so we can pass them into the Simplify method
            // When the pooled object leaves the scope it will be Disposed and returned to the pool automatically.
            // This version is ideal for working with temporary lists.
            using (CollectionPool<List<[Vector2](Vector2.html)>, [Vector2](Vector2.html)>.Get(out List<[Vector2](Vector2.html)> tempList))
            {
                for (int i = 0; i < points.Length; ++i)
                {
                    tempList.Add(points[i]);
                }  
      
                [LineUtility.Simplify](LineUtility.Simplify.html)(tempList, 1.5f, simplifiedPoints);
            }
            return simplifiedPoints;
        }
    }
    

* * *

## Declaration

public static PooledObject<TCollection> Get(out TCollection value);

### Parameters

value | Out parameter that will contain a reference to an instance from the pool.  
---|---  
  
### Returns

**PooledObject <TCollection>** A PooledObject that will return the instance
back to the pool when its Dispose method is called.

### Description

Returns a PooledObject that will automatically return the instance to the pool
when it is disposed.

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

