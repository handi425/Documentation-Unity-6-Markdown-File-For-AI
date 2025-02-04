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

#  [LineUtility](LineUtility.html).Simplify

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

public static void Simplify(List<Vector3> points, float tolerance, List<int>
pointsToKeep);

## Declaration

public static void Simplify(List<Vector3> points, float tolerance,
List<Vector3> simplifiedPoints);

## Declaration

public static void Simplify(List<Vector2> points, float tolerance, List<int>
pointsToKeep);

## Declaration

public static void Simplify(List<Vector2> points, float tolerance,
List<Vector2> simplifiedPoints);

### Parameters

points | The points that make up the original line.  
---|---  
tolerance | This value is used to evaluate which points should be removed from the line. A higher value results in a simpler line (less points). A positive value close to zero results in a line with little to no reduction. A value of zero or less has no effect.  
pointsToKeep | Populated by this function. Contains the indexes of the points that should be generate a simplified version..  
simplifiedPoints | Populated by this function. Contains the points that form the simplified line.  
  
### Description

Generates a simplified version of the original line by removing points that
fall within the specified tolerance.

As an example, you can use this function for reducing a complex line made up
of thousands of points. The line can be reduced to hundreds or even less
points and still maintain a form closely matching the original. You can
generate multiple versions of the same line with varying detail levels by
adjusting the tolerance (higher tolerance values results in less points in the
generated line). The generated line can then be displayed using the LODGroup
system.  
  
The Simplify algorithm is based on the [Ramer Douglas Peucker
algorithm](https://en.wikipedia.org/wiki/Ramer-Douglas-Peucker_algorithm) ; it
creates a line that closely represents the provided line but with fewer
points(determined by tolerance).  
  
**Note:** This function can handle a large number of points as it is non-
recursive. The 2D version of this function performs better than this function
as it uses a simpler way to evaluate the points.  
  
Additional resources: [LineRenderer.Simplify](LineRenderer.Simplify.html).  
  
**The following example shows how to apply line simplification to an existing
line.**

    
    
    using System.Collections.Generic;
    using System.Linq;
    using UnityEngine;  
      
    // This example shows how to apply line simplification to a line that already contains points.
    [[RequireComponent](RequireComponent.html)(typeof([LineRenderer](LineRenderer.html)))]
    public class SimpleExampleLineUtility : [MonoBehaviour](MonoBehaviour.html)
    {
        public float tolerance = 1;
        void Start()
        {
            // Get the points.
            var lineRenderer = GetComponent<[LineRenderer](LineRenderer.html)>();
            int pointsBefore = lineRenderer.positionCount;
            var points = new [Vector3](Vector3.html)[pointsBefore];
            lineRenderer.GetPositions(points);  
      
            // Simplify.
            var simplifiedPoints = new List<[Vector3](Vector3.html)>();
            [LineUtility.Simplify](LineUtility.Simplify.html)(points.ToList(), tolerance, simplifiedPoints);  
      
            // Assign back to the line renderer.
            lineRenderer.positionCount = simplifiedPoints.Count;
            lineRenderer.SetPositions(simplifiedPoints.ToArray());  
      
            [Debug.Log](Debug.Log.html)("Line reduced from " + pointsBefore + " to " + lineRenderer.positionCount);
        }
    }
    

The following example shows how the pointsToKeep parameter can be used to
return a list of indices. The list can then be used to simplify a line that
retains points in that list. Additional points can still be added on to the
resulting simplified line.

    
    
    using System.Collections.Generic;
    using System.Linq;
    using UnityEngine;  
      
    // This example shows how to use the pointsToKeep parameter to generate a new simplified version of the line.
    [[RequireComponent](RequireComponent.html)(typeof([LineRenderer](LineRenderer.html)))]
    public class SimpleExampleLineUtilityPointsToKeep : [MonoBehaviour](MonoBehaviour.html)
    {
        public float tolerance = 1;
        void Start()
        {
            // Get the points.
            var lineRenderer = GetComponent<[LineRenderer](LineRenderer.html)>();
            int pointsBefore = lineRenderer.positionCount;
            var points = new [Vector3](Vector3.html)[pointsBefore];
            lineRenderer.GetPositions(points);  
      
            // Simplify.
            var pointsToKeep = new List<int>();
            [LineUtility.Simplify](LineUtility.Simplify.html)(points.ToList(), tolerance, pointsToKeep);  
      
            var simplifiedPoints = new [Vector3](Vector3.html)[pointsToKeep.Count];
            for (int i = 0; i < simplifiedPoints.Length; ++i)
            {
                simplifiedPoints[i] = points[pointsToKeep[i]];
            }  
      
            // Assign back to the line renderer.
            lineRenderer.positionCount = simplifiedPoints.Length;
            lineRenderer.SetPositions(simplifiedPoints);  
      
            [Debug.Log](Debug.Log.html)("Line reduced from " + pointsBefore + " to " + lineRenderer.positionCount);
        }
    }
    

This example generates a line in the shape of a sine wave and provides a GUI
for customizing the line generation and simplification parameters.

    
    
    using System.Collections.Generic;
    using UnityEngine;  
      
    // This example creates a sine wave and then simplifies it using the [LineUtility](LineUtility.html).
    // The parameters can be adjusted through an in game [GUI](GUI.html) to allow for experimentation.
    [[RequireComponent](RequireComponent.html)(typeof([LineRenderer](LineRenderer.html)))]
    public class LineUtilityExample : [MonoBehaviour](MonoBehaviour.html)
    {
        public int numberOfPoints = 1000;
        public float length = 50;
        public float waveHeight = 10;
        public float tolerance = 0.1f;  
      
        private [LineRenderer](LineRenderer.html) lineRenderer;
        private List<[Vector3](Vector3.html)> points = new List<[Vector3](Vector3.html)>(); // Generated points before LineOptimizer is used.
        private List<[Vector3](Vector3.html)> simplifiedPoints = new List<[Vector3](Vector3.html)>(); // Simplified points after LineOptimizer is used.  
      
        public void Start()
        {
            lineRenderer = GetComponent<[LineRenderer](LineRenderer.html)>();
        }  
      
        // Generates the sine wave points.
        public void GeneratePoints()
        {
            points.Clear();
            float halfWaveHeight = waveHeight * 0.5f;
            float step = length / numberOfPoints;
            for (int i = 0; i < numberOfPoints; ++i)
            {
                points.Add(new [Vector3](Vector3.html)(i * step, [Mathf.Sin](Mathf.Sin.html)(i * step) * halfWaveHeight, 0));
            }
        }  
      
        // Simplify the line using the LineOptimizer.
        public void SimplifyLine()
        {
            simplifiedPoints.Clear();
            [LineUtility.Simplify](LineUtility.Simplify.html)(points, tolerance, simplifiedPoints);
            lineRenderer.positionCount = simplifiedPoints.Count;
            lineRenderer.SetPositions(simplifiedPoints.ToArray());
        }  
      
        // Draw a simple [GUI](GUI.html) slider with a label.
        private static float GUISlider(string label, float value, float min, float max)
        {
            [GUILayout.BeginHorizontal](GUILayout.BeginHorizontal.html)([GUILayout.Width](GUILayout.Width.html)([Screen.width](Screen-width.html) / 2.0f));
            [GUILayout.Label](GUILayout.Label.html)(label + "(" + value + ") :", [GUILayout.Width](GUILayout.Width.html)(150));
            var val = [GUILayout.HorizontalSlider](GUILayout.HorizontalSlider.html)(value, min, max);
            [GUILayout.EndHorizontal](GUILayout.EndHorizontal.html)();
            return val;
        }  
      
        public void OnGUI()
        {
            [GUILayout.Label](GUILayout.Label.html)("[LineUtility.Simplify](LineUtility.Simplify.html)", GUI.skin.box);  
      
            // We use [GUI.changed](GUI-changed.html) to detect if a value was changed via the [GUI](GUI.html), if it has we can then re-generate the points and simplify the line again.
            [GUI.changed](GUI-changed.html) = false;  
      
            numberOfPoints = (int)GUISlider("Number of Points", numberOfPoints, 0, 1000);
            length = GUISlider("[Length](UIElements.Length.html)", length, 0, 100);
            waveHeight = GUISlider("Wave Height", waveHeight, 0, 100);
            if ([GUI.changed](GUI-changed.html))
                GeneratePoints();  
      
            tolerance = GUISlider("Simplify Tolerance", tolerance, 0, 2);
            if ([GUI.changed](GUI-changed.html))
                SimplifyLine();  
      
            float percentRemoved = 100.0f - ((float)lineRenderer.positionCount / numberOfPoints) * 100.0f;
            if (tolerance > 0.0f)
                [GUILayout.Label](GUILayout.Label.html)("Points after simplification: " + lineRenderer.positionCount + "(Removed " + percentRemoved.ToString("##.##") + "%)");
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

